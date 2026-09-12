"""Process-free R34 compatibility controls; binding objects are test data only.

CGDR_AD_INPUT points to the exact AD input tree (matrix and retained baseline).
No main(), run(), episode, worker, helper, subprocess or network is invoked.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

from cgdr_r1_6b import logic_path, observer, observer_fixtures


class SelectedProcessMatrixR16ADTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(os.environ['CGDR_AD_INPUT']).resolve()
        matrix_bytes = (root / 'profile/TRANSITION_TEST_MATRIX.json').read_bytes()
        baseline_bytes = (root / 'baseline/BASELINE_CODE_BINDINGS_R1_6X_SUCCESSOR.json').read_bytes()
        cls.matrix = json.loads(matrix_bytes)
        cls.hashes = {
            'matrix_sha256': hashlib.sha256(matrix_bytes).hexdigest(),
            'successor_baseline_sha256': hashlib.sha256(baseline_bytes).hexdigest(),
        }
        assert cls.hashes['matrix_sha256'] == '7288a4e60501d1c8209308dacc4450e3d046f20b51ad5a8ad05f9010b4239a60'
        assert cls.hashes['successor_baseline_sha256'] == 'd32f1e3e70146052f425256bf69c5debeed39cc57a9b628136779dc8d3df9a73'
        with tempfile.TemporaryDirectory(prefix='ad-positive-trace-') as tmp:
            cls.protected_trace = observer_fixtures.positive_trace(Path(tmp) / 'test-keys')

    def legacy(self):
        return copy.deepcopy(self.protected_trace)

    def assert_scope(self, evidence, value, reason):
        self.assertEqual(observer.review_execution_scope(evidence),
                         observer.RuleResult(value, ('scope',), reason))

    def assert_ambiguous(self, evidence):
        self.assert_scope(evidence, 'FAIL', 'EXECUTION_SCOPE_EXECUTION_MODES_AMBIGUOUS')

    def scope(self, mode):
        # Static synthetic coordinate for validation only; never a runtime ID.
        run_id = 'ad-offline-binding-control'
        cells = [c['cell_id'] for c in self.matrix['cells']] if mode == 'FULL_MATRIX' else ['T0']
        binding = {
            'schema': 'CGDR_SELECTED_PROCESS_EXECUTION_SCOPE_BINDING_V1',
            'status': 'OWNER_AUTHORIZED', 'owner_task_id': 'AD_OFFLINE_TEST_ONLY',
            'authorization_ref': 'TEST_ONLY:NOT_RUNTIME_AUTHORITY',
            'profile_id': 'CGDR-R1.6A-SELECTED-PROCESS', 'profile_binding': 'PROFILE_BINDING_C1',
            'mode': mode, 'matrix_run_id': run_id, 'allowed_cells': cells,
            'allowed_checkpoints': [
                {'cell_id': c['cell_id'], 'checkpoint': p['checkpoint']}
                for c in self.matrix['cells'] if c['cell_id'] in cells
                for p in c['expected_checkpoints']
            ],
            'final_matrix_credit': mode == 'FULL_MATRIX', **self.hashes,
        }
        return {
            **observer.execution_scope_evidence(binding, matrix_run_id=run_id, **self.hashes),
            'profile_id': binding['profile_id'], 'matrix_run_id': run_id,
            'cell_id': 'T0', 'checkpoint': 'OPEN_CHECK',
        }

    def test_ad01_protected_positive_trace_r34_pass(self):
        result = observer.inspect_checkpoint(self.legacy())
        self.assertEqual(result['observer_status'], 'PASS')
        r34 = next(a for a in result['assertions'] if a['requirement_id'] == 'R34')
        self.assertEqual((r34['value'], r34['reason']), ('PASS', 'NO_MATRIX_OR_NEW_ARCHITECTURE'))
        self.assertEqual([a for a in result['assertions'] if a['value'] not in ('PASS', 'NOT_APPLICABLE')], [])

    def test_ad02_protected_logic_path_all_eight_pass(self):
        with tempfile.TemporaryDirectory(prefix='ad-logic-path-') as tmp:
            result = logic_path.execute(Path(tmp) / 'synthetic-output')
        self.assertEqual(result['offline_logic_path_status'], 'PASS')
        self.assertEqual(result['checks'], {
            'open_hold_zero': True, 'resolved_allow_one': True, 'zero_promotions': True,
            'observer_logic_path': True, 'observer_19_controls': True,
            'observer_d02_d05': True, 'native_four_layers': True, 'e01_e05_controls': True,
        })
        self.assertEqual([result[k] for k in ('worker_start_requests', 'helper_starts', 'wsl_launches')], [0, 0, 0])
        self.assertEqual(result['selected_process_conformance'], 'NOT_RUN')
        self.assertIsNone(result['matrix_effects'])
        self.assertIsNone(result['matrix_promotions'])

    def test_ad03_explicit_no_run_requires_clean_exact_shape(self):
        evidence = {'measured_matrix_started': False, 'matrix_canary_started': False, 'evidence_scope': 'OFFLINE_VALIDATION'}
        self.assert_scope(evidence, 'PASS', 'NO_MATRIX_OR_NEW_ARCHITECTURE')
        self.assert_scope({**evidence, 'final_matrix_credit': False}, 'PASS', 'NO_MATRIX_OR_NEW_ARCHITECTURE')
        for key in ('matrix_run_id', 'execution_scope_binding', 'execution_scope_binding_hash',
                    'actual_matrix_sha256', 'actual_successor_baseline_sha256',
                    'execution_owner_task_id', 'execution_authorization_ref', 'profile_binding'):
            for value in (None, '', 'residue'):
                with self.subTest(key=key, value=value):
                    self.assert_ambiguous({**evidence, key: value})
        for value in (None, 0, True):
            with self.subTest(credit=value):
                self.assert_ambiguous({**evidence, 'final_matrix_credit': value})
        for key in ('measured_matrix_started', 'matrix_canary_started'):
            for value in (None, 0):
                with self.subTest(key=key, value=value):
                    self.assert_ambiguous({**evidence, key: value})
        for scope in ('MEASURED_MATRIX_CHECKPOINT', 'MATRIX_CANARY_CHECKPOINT'):
            with self.subTest(scope=scope):
                self.assert_ambiguous({**evidence, 'evidence_scope': scope})

    def test_ad04_exact_legacy_missing_canary_pass(self):
        evidence = self.legacy()
        self.assertIs(evidence['measured_matrix_started'], False)
        self.assertEqual(evidence['evidence_scope'], 'SYNTHETIC_REGRESSION')
        self.assertNotIn('matrix_canary_started', evidence)
        self.assertNotIn('final_matrix_credit', evidence)
        self.assert_scope(evidence, 'PASS', 'NO_MATRIX_OR_NEW_ARCHITECTURE')
        self.assert_scope({**evidence, 'final_matrix_credit': False}, 'PASS', 'NO_MATRIX_OR_NEW_ARCHITECTURE')

    def test_ad05_legacy_present_null_canary_fails(self):
        self.assert_ambiguous({**self.legacy(), 'matrix_canary_started': None})

    def test_ad06_legacy_integer_zero_canary_fails(self):
        self.assert_ambiguous({**self.legacy(), 'matrix_canary_started': 0})

    def test_ad07_legacy_integer_zero_measured_fails(self):
        self.assert_ambiguous({**self.legacy(), 'measured_matrix_started': 0})

    def test_ad08_legacy_matrix_run_id_presence_fails(self):
        for value in ('ad-offline-binding-control', '', None):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'matrix_run_id': value})

    def test_ad09_legacy_binding_presence_including_null_fails(self):
        for value in (None, {}, False, self.scope('CANARY')['execution_scope_binding']):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'execution_scope_binding': value})

    def test_ad10_legacy_binding_hash_residue_fails(self):
        for value in ('0' * 64, None):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'execution_scope_binding_hash': value})

    def test_ad11_legacy_actual_matrix_hash_residue_fails(self):
        for value in (self.hashes['matrix_sha256'], None):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'actual_matrix_sha256': value})

    def test_ad12_legacy_actual_baseline_hash_residue_fails(self):
        for value in (self.hashes['successor_baseline_sha256'], None):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'actual_successor_baseline_sha256': value})

    def test_ad13_legacy_owner_or_reference_residue_fails(self):
        for key in ('execution_owner_task_id', 'execution_authorization_ref'):
            for value in ('TEST_ONLY', None):
                with self.subTest(key=key, value=value):
                    self.assert_ambiguous({**self.legacy(), key: value})

    def test_ad14_legacy_profile_binding_residue_fails(self):
        for value in ('PROFILE_BINDING_C1', None):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'profile_binding': value})

    def test_ad15_legacy_final_credit_must_be_exact_false_or_absent(self):
        for value in (True, None, 0, ''):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'final_matrix_credit': value})

    def test_ad16_missing_canary_unknown_or_missing_scope_fails(self):
        for value in ('UNKNOWN', 'OFFLINE_VALIDATION', '', None):
            with self.subTest(value=value):
                self.assert_ambiguous({**self.legacy(), 'evidence_scope': value})
        evidence = self.legacy(); del evidence['evidence_scope']
        self.assert_ambiguous(evidence)

    def test_ad17_missing_canary_measured_label_fails(self):
        self.assert_ambiguous({**self.legacy(), 'evidence_scope': 'MEASURED_MATRIX_CHECKPOINT'})

    def test_ad18_missing_canary_canary_label_fails(self):
        self.assert_ambiguous({**self.legacy(), 'evidence_scope': 'MATRIX_CANARY_CHECKPOINT'})

    def test_ad19_bound_canary_remains_pass_without_final_credit(self):
        evidence = self.scope('CANARY')
        self.assertIs(evidence['measured_matrix_started'], False)
        self.assertIs(evidence['matrix_canary_started'], True)
        self.assertIs(evidence['final_matrix_credit'], False)
        self.assert_scope(evidence, 'PASS', 'BOUNDED_OWNER_AUTHORIZATION_BOUND')

    def test_ad20_bound_full_matrix_remains_pass_with_final_credit(self):
        evidence = self.scope('FULL_MATRIX')
        self.assertIs(evidence['measured_matrix_started'], True)
        self.assertIs(evidence['matrix_canary_started'], False)
        self.assertIs(evidence['final_matrix_credit'], True)
        self.assertEqual(len(evidence['execution_scope_binding']['allowed_cells']), 18)
        self.assertEqual(len(evidence['execution_scope_binding']['allowed_checkpoints']), 21)
        self.assert_scope(evidence, 'PASS', 'BOUNDED_OWNER_AUTHORIZATION_BOUND')

    def test_ad21_canary_wrong_coordinate_remains_fail(self):
        for key, value in (('cell_id', 'N0'), ('checkpoint', 'fault')):
            with self.subTest(key=key):
                self.assert_scope({**self.scope('CANARY'), key: value}, 'FAIL', 'EXECUTION_SCOPE_COORDINATE_NOT_AUTHORIZED')

    def test_ad22_wrong_matrix_or_baseline_hash_remains_fail(self):
        for mode in ('CANARY', 'FULL_MATRIX'):
            for key, reason in (
                ('actual_matrix_sha256', 'EXECUTION_SCOPE_MATRIX_SHA256_MISMATCH'),
                ('actual_successor_baseline_sha256', 'EXECUTION_SCOPE_SUCCESSOR_BASELINE_SHA256_MISMATCH'),
            ):
                with self.subTest(mode=mode, key=key):
                    self.assert_scope({**self.scope(mode), key: '0' * 64}, 'FAIL', reason)

    def test_ad23_canary_without_binding_remains_fail(self):
        evidence = self.scope('CANARY'); del evidence['execution_scope_binding']
        self.assert_scope(evidence, 'FAIL', 'EXECUTION_SCOPE_BINDING_MISSING')

    def test_ad24_measured_without_binding_remains_fail(self):
        evidence = self.scope('FULL_MATRIX'); del evidence['execution_scope_binding']
        self.assert_scope(evidence, 'FAIL', 'EXECUTION_SCOPE_BINDING_MISSING')
