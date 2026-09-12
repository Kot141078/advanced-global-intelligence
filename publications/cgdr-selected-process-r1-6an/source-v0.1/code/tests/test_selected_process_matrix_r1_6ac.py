"""Process-free AC controls. CGDR_AC_INPUT binds the immutable exact input tree.

All scope objects below are TEST-ONLY counterfactuals, never execution authority.
No worker, subprocess, run(), main(), _run_episode() or canary is invoked here.
"""
from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import os
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cgdr_r1_6b import observer, producer, run_batch
from cgdr_r1_6b.common import canonical_hash
from cgdr_r1_6b.receiver import evaluate
from cgdr_r1_6b.signing import TestKeyStore, verify
from cgdr_r1_6b.state_transfer import MATERIAL_FIELDS, material_projection


class MemoryKeys(TestKeyStore):
    """Ephemeral test signing only; no private key files or credential reads."""
    def __init__(self):
        self.keys = {}

    def ensure(self, key_id):
        if key_id not in self.keys:
            self.keys[key_id] = Ed25519PrivateKey.generate()
        return self.keys[key_id]


def load_predecessor(input_root, name):
    path = input_root / ('code/src/cgdr_r1_6b/' + name + '.py')
    manifest = json.loads((input_root / 'MANIFEST_CURRENT_X.json').read_text())
    row = next(x for x in manifest['files'] if x['path'] == 'src/cgdr_r1_6b/' + name + '.py')
    assert len(path.read_bytes()) == row['bytes'] and hashlib.sha256(path.read_bytes()).hexdigest() == row['sha256']
    module_name = 'cgdr_r1_6b._ac_predecessor_' + name
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class SelectedProcessMatrixR16ACTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input = Path(os.environ['CGDR_AC_INPUT']).resolve()
        cls.matrix_path = cls.input / 'profile/TRANSITION_TEST_MATRIX.json'
        cls.baseline_path = cls.input / 'runtime_inputs/BASELINE_CODE_BINDINGS_R1_6X_SUCCESSOR.json'
        cls.matrix = cls.read('profile/TRANSITION_TEST_MATRIX.json')
        cls.raw = {c: cls.read('ab_evidence/raw/' + c + '.json') for c in ('OPEN_CHECK', 'RESOLVED_CHECK')}
        cls.saved = cls.read('ab_evidence/SAVED_EVIDENCE_REVIEW.json')
        cls.episode = cls.read('ab_evidence/EPISODE_RESULT.json')
        cls.old_observer = load_predecessor(cls.input, 'observer')
        cls.old_batch = load_predecessor(cls.input, 'run_batch')
        cls.keys = MemoryKeys()
        cls.public = cls.keys.public_map({'producer-alpha': 'root:alpha', 'approver-beta': 'root:beta',
                                         'alias-alpha-1': 'root:alpha', 'alias-alpha-2': 'root:alpha'})

    @classmethod
    def read(cls, relative):
        return json.loads((cls.input / relative).read_text(encoding='utf-8'))

    @classmethod
    def hashes(cls):
        return {'matrix_sha256': hashlib.sha256(cls.matrix_path.read_bytes()).hexdigest(),
                'successor_baseline_sha256': hashlib.sha256(cls.baseline_path.read_bytes()).hexdigest()}

    @classmethod
    def alignment(cls, checkpoint):
        raw = cls.raw[checkpoint]
        saved = cls.saved
        evidence = cls.read('ab_evidence/evidence/' + checkpoint + '.json')
        obs = evidence['observer']; source = raw['source_inventory']
        return {
            **{k: raw[k] for k in ('matrix_run_id', 'cell_id', 'checkpoint', 'attempt_id', 'active_instance_id', 'lifecycle_mode')},
            'lifecycle_steps': cls.episode['lifecycle_steps'], 'w0_instance_id': saved['e0']['instance_id'],
            'w1_instance_id': saved['e1']['instance_id'], 'w0_cleanup': saved['cleanup']['W0']['status'],
            'state_carriage': 'PASS' if saved['state_carriage']['all_equal'] else 'FAIL',
            'current_epoch': source['current_attestation']['epoch'], 'e0_status': saved['e0']['status'],
            'readiness': 'READY' if saved['readiness_before_authorization'] else None,
            'implementation_freeze': saved['implementation_freeze']['stage'], 'capture_gaps': saved['observer_gaps'],
            'writer_admission': evidence['actual']['admission'],
            'expected_effect_delta': evidence['expected']['protected_effect_delta'], 'actual_effect_delta': obs['actual_effect_delta'],
            'expected_promotion_delta': evidence['expected']['confirmed_EA_delta'], 'actual_promotion_delta': obs['actual_promotion_delta'],
            'approval_roots': obs['derived_gate']['approvals']['roots'], 'required_approval_roots': obs['derived_gate']['approvals']['required'],
            'q_state': obs['derived_gate']['q_state'], 'qcr_valid': bool(source.get('resolution')),
            'expected_obligations': source['duty']['liabilities'], 'carried_obligations': raw['materialized_packet']['duty']['liabilities'],
            'evidence_binding': {k: raw[k] for k in ('matrix_run_id', 'cell_id', 'checkpoint', 'attempt_id')},
            'attempt_coverage_complete': True, 'registry_coverage_complete': True, 'surface_inventory': raw['surface_observations'],
        }

    @classmethod
    def binding(cls, mode='CANARY'):
        cells = [x['cell_id'] for x in cls.matrix['cells']] if mode == 'FULL_MATRIX' else ['T0']
        return {'schema': 'CGDR_SELECTED_PROCESS_EXECUTION_SCOPE_BINDING_V1', 'status': 'OWNER_AUTHORIZED',
                'owner_task_id': 'AC_OFFLINE_COUNTERFACTUAL_ONLY', 'authorization_ref': 'TEST_ONLY:NOT_RUNTIME_AUTHORITY',
                'profile_id': 'CGDR-R1.6A-SELECTED-PROCESS', 'profile_binding': 'PROFILE_BINDING_C1',
                'mode': mode, 'matrix_run_id': cls.raw['OPEN_CHECK']['matrix_run_id'], 'allowed_cells': cells,
                'allowed_checkpoints': [{'cell_id': c['cell_id'], 'checkpoint': p['checkpoint']}
                                        for c in cls.matrix['cells'] if c['cell_id'] in cells for p in c['expected_checkpoints']],
                'final_matrix_credit': mode == 'FULL_MATRIX', **cls.hashes()}

    @classmethod
    def scope(cls, mode='CANARY'):
        b = cls.binding(mode)
        return {**observer.execution_scope_evidence(b, matrix_run_id=b['matrix_run_id'], **cls.hashes()),
                'profile_id': b['profile_id'], 'matrix_run_id': b['matrix_run_id'], 'cell_id': 'T0', 'checkpoint': 'OPEN_CHECK'}

    @classmethod
    def proposal_packet(cls, checkpoint='OPEN_CHECK', cell='T0'):
        raw = cls.raw[checkpoint]; source = copy.deepcopy(raw['source_inventory'])
        # Exact AB source, with the existing producer fault branch selected by cell.
        return producer.make_packet(cell, source, cls.keys, checkpoint,
            instance_id=raw['active_instance_id'], attempt_id=raw['attempt_id'],
            operation_id=raw['operation_id'], commit_record_id=raw['commit_record_id']), source

    @classmethod
    def counterfactual(cls, checkpoint):
        raw = copy.deepcopy(cls.raw[checkpoint]); old_hash = raw['proposal_hash']
        p = producer._projection(raw['source_inventory'], 'T0', checkpoint, raw['active_instance_id'],
                                 raw['attempt_id'], raw['operation_id'], raw['commit_record_id'])
        p['proposal_hash'] = canonical_hash(p)
        # Rebind only the hypothetical proposal and its existing hash references.
        # Original source, chronology, approvals and effect coordinate remain exact.
        def replace(value, before, after):
            if isinstance(value, dict): return {k: replace(v, before, after) for k, v in value.items()}
            if isinstance(value, list): return [replace(v, before, after) for v in value]
            return after if value == before else value
        raw = replace(raw, old_hash, p['proposal_hash'])
        raw['materialized_packet'] = p
        raw['materialized_packet_hash'] = canonical_hash(p)
        old_intent_hash = raw['operation_intent_hash']
        raw = replace(raw, old_intent_hash, canonical_hash(raw['operation_intent']))
        raw.update(observer.execution_scope_evidence(cls.binding(), matrix_run_id=raw['matrix_run_id'], **cls.hashes()))
        return raw

    def assert_scope_fails(self, evidence):
        result = observer.review_execution_scope(evidence)
        self.assertEqual(result.value, 'FAIL', result)

    def test_ac01_exact_predecessor_open_sole_o05(self):
        result = self.old_batch.review_alignment_evidence(self.alignment('OPEN_CHECK'))
        self.assertEqual(result, {'verdict': 'FAIL', 'issues': [{'code': 'O05_ALIAS_ROOTS_NOT_INDEPENDENT', 'classification': 'FAIL'}]})

    def test_ac02_exact_predecessor_both_observers(self):
        for c, raw in self.raw.items():
            result = self.old_observer.inspect_checkpoint(raw)
            self.assertEqual(result, self.read('ab_evidence/evidence/' + c + '.json')['observer'])
            self.assertEqual([x['requirement_id'] for x in result['assertions'] if x['value'] == 'FAIL'], ['R16', 'R21', 'R31', 'R34'])

    def test_ac03_open_alignment_pass_without_lowering_policy(self):
        value = self.alignment('OPEN_CHECK')
        self.assertEqual(value['required_approval_roots'], 2)
        self.assertIs(value['qcr_valid'], False)
        self.assertEqual(run_batch.review_alignment_evidence(value), {'verdict': 'PASS_ALIGNED_EPISODE', 'issues': []})

    def test_ac04_resolved_distinct_roots_pass(self):
        value = self.alignment('RESOLVED_CHECK')
        self.assertEqual(value['approval_roots'], ['root:alpha', 'root:beta'])
        self.assertEqual(run_batch.review_alignment_evidence(value)['verdict'], 'PASS_ALIGNED_EPISODE')

    def test_ac05_t5a_alias_roots_fail(self):
        packet, source = self.proposal_packet('RESOLVED_CHECK', 'T5A')
        value = self.alignment('RESOLVED_CHECK')
        value['approval_roots'] = [x['protected']['principal_root'] for x in packet['approvals']]
        self.assertEqual(len(value['approval_roots']), 3)
        self.assertEqual(len(set(value['approval_roots'])), 1)
        self.assertIn('DISTINCT_APPROVAL_ROOTS_INSUFFICIENT', evaluate(packet, source, self.public)['failures'])
        self.assertIn('O05_ALIAS_ROOTS_NOT_INDEPENDENT', [x['code'] for x in run_batch.review_alignment_evidence(value)['issues']])

    def test_ac06_false_collapse_still_o06(self):
        value = self.alignment('OPEN_CHECK'); value['q_state'] = 'COLLAPSED_SCOPED'
        self.assertIn('O06_OPEN_QFR_FALSE_COLLAPSE', [x['code'] for x in run_batch.review_alignment_evidence(value)['issues']])

    def assert_material_packet(self, checkpoint):
        packet, source = self.proposal_packet(checkpoint); p = packet['envelope']['payload']
        self.assertEqual({k: p[k] for k in MATERIAL_FIELDS}, material_projection(source))
        self.assertEqual(p['proposal_hash'], canonical_hash({k: v for k, v in p.items() if k != 'proposal_hash'}))
        self.assertEqual(packet['transport_hash'], canonical_hash({k: packet[k] for k in ('envelope', 'approvals')}))
        self.assertTrue(verify(packet['envelope'], self.public)[0])
        self.assertEqual(len(packet['approvals']), 0 if checkpoint == 'OPEN_CHECK' else 2)
        p['qsf']['variants'].clear()
        self.assertNotEqual(p['qsf'], source['qsf'])

    def test_ac07_open_carries_every_material_field(self): self.assert_material_packet('OPEN_CHECK')
    def test_ac08_resolved_carries_every_material_field(self): self.assert_material_packet('RESOLVED_CHECK')

    def assert_fault(self, cell, failure, checkpoint='OPEN_CHECK'):
        packet, source = self.proposal_packet(checkpoint, cell)
        result = evaluate(packet, source, self.public)
        self.assertIn(failure, result['failures'])
        self.assertNotEqual(result['action_gate'], 'ALLOW')

    def test_ac09_t1_receiver_omission_detected(self): self.assert_fault('T1', 'RECEIVER_BASIS_MISSING_OR_CHANGED')
    def test_ac10_t2q_qsf_omission_detected(self): self.assert_fault('T2Q', 'ACTIVE_QSF_MISSING')
    def test_ac11_t2d_minority_variant_loss_detected(self): self.assert_fault('T2D', 'QSF_VARIANT_OR_DISPUTE_INCOMPLETE')
    def test_ac12_t3_duty_omission_detected(self): self.assert_fault('T3', 'DUTY_CARRIAGE_MISMATCH')
    def test_ac13_t6_role_expansion_detected(self): self.assert_fault('T6', 'ROLE_SURFACE_MISMATCH')
    def test_ac14_t7_stale_epoch_detected(self): self.assert_fault('T7', 'CURRENT_ATTESTATION_MISMATCH')

    def test_ac15_t8_promotion_request_retained(self):
        packet, source = self.proposal_packet(cell='T8')
        self.assertEqual(packet['envelope']['payload']['memory_request'], 'PROMOTE_QUARANTINED_TO_CONFIRMED_EA')
        decision = evaluate(packet, source, self.public)
        self.assertIs(decision['memory_promotion_authorized'], False)
        self.assertNotEqual(decision['action_gate'], 'ALLOW')

    def test_ac16_counterfactual_open_only_lawful_r28_pending(self):
        result = observer.inspect_checkpoint(self.counterfactual('OPEN_CHECK'))
        self.assertEqual(result['problems'], [])
        self.assertEqual([x for x in result['assertions'] if x['value'] == 'FAIL'], [])
        self.assertEqual([(x['requirement_id'], x['reason']) for x in result['assertions'] if x['value'] == 'UNKNOWN'],
                         [('R28', 'RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD')])

    def test_ac17_counterfactual_resolved_pass(self):
        self.assertEqual(observer.inspect_checkpoint(self.counterfactual('RESOLVED_CHECK'))['observer_status'], 'PASS')

    def test_ac18_counterfactual_linked_logic_pass(self):
        result = observer.inspect_logic_path(self.counterfactual('OPEN_CHECK'), self.counterfactual('RESOLVED_CHECK'))
        self.assertEqual(result['offline_logic_path_status'], 'PASS')
        self.assertEqual(result['in_scope_failures'], [])
        self.assertEqual(result['in_scope_unknowns'], [])
        self.assertTrue(all(result['checks'].values()))

    def test_ac19_no_run_without_binding_passes(self):
        result = observer.review_execution_scope({'measured_matrix_started': False, 'matrix_canary_started': False})
        self.assertEqual((result.value, result.reason), ('PASS', 'NO_MATRIX_OR_NEW_ARCHITECTURE'))

    def test_ac20_bound_canary_passes(self):
        self.assertEqual(observer.review_execution_scope(self.scope()).value, 'PASS')

    def test_ac21_bound_full_matrix_passes(self):
        e = self.scope('FULL_MATRIX')
        self.assertEqual(len(e['execution_scope_binding']['allowed_cells']), 18)
        self.assertEqual(len(e['execution_scope_binding']['allowed_checkpoints']), 21)
        self.assertEqual(observer.review_execution_scope(e).value, 'PASS')

    def test_ac22_missing_binding_fails(self):
        e = self.scope(); del e['execution_scope_binding']; self.assert_scope_fails(e)

    def test_ac23_hash_mismatch_fails(self):
        e = self.scope(); e['execution_scope_binding_hash'] = '0' * 64; self.assert_scope_fails(e)

    def test_ac24_foreign_coordinates_fail(self):
        for field, value in [('matrix_run_id', 'foreign-run-001'), ('profile_id', 'FOREIGN'), ('profile_binding', 'FOREIGN'),
                             ('cell_id', 'N0'), ('checkpoint', 'fault'), ('execution_owner_task_id', 'FOREIGN'),
                             ('execution_authorization_ref', 'FOREIGN')]:
            with self.subTest(field=field):
                e = self.scope(); e[field] = value; self.assert_scope_fails(e)

    def test_ac25_wrong_modes_and_credit_fail(self):
        for field, value in [('final_matrix_credit', True), ('final_matrix_credit', 0), ('measured_matrix_started', True),
                             ('matrix_canary_started', False), ('evidence_scope', 'MEASURED_MATRIX_CHECKPOINT')]:
            with self.subTest(field=field, value=value):
                e = self.scope(); e[field] = value; self.assert_scope_fails(e)
        for value in ('FULL_MATRIX', 'NO_RUN', '', None, True):
            e = self.scope(); e['execution_scope_binding']['mode'] = value
            e['execution_scope_binding_hash'] = canonical_hash(e['execution_scope_binding']); self.assert_scope_fails(e)

    def test_ac26_matrix_and_baseline_hash_mismatches_fail(self):
        for field in ('matrix_sha256', 'successor_baseline_sha256'):
            e = self.scope(); e['execution_scope_binding'][field] = '0' * 64
            e['execution_scope_binding_hash'] = canonical_hash(e['execution_scope_binding']); self.assert_scope_fails(e)
            e = self.scope(); e['actual_' + field] = '0' * 64; self.assert_scope_fails(e)

    def args(self, binding_path=None):
        return Namespace(execution_scope_binding=binding_path, execute_authorized=True, matrix=self.matrix_path,
                         successor_baseline=self.baseline_path, matrix_run_id=self.raw['OPEN_CHECK']['matrix_run_id'])

    def test_ac27_full_partial_and_duplicate_inventory_fails_before_runtime(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'binding.json'
            for field in ('allowed_cells', 'allowed_checkpoints'):
                for duplicate in (False, True):
                    b = self.binding('FULL_MATRIX')
                    if duplicate: b[field][-1] = copy.deepcopy(b[field][0])
                    else: b[field].pop()
                    path.write_text(json.dumps(b), encoding='utf-8')
                    with self.subTest(field=field, duplicate=duplicate), self.assertRaises(ValueError):
                        run_batch.prepare_execution_scope(self.args(path))
            self.assertEqual(sorted(p.name for p in Path(d).iterdir()), ['binding.json'])

    def test_ac28_positive_prospective_verdict_valid_and_unrelabeled(self):
        review = self.read('ab_evidence/PROSPECTIVE_OBSERVATION_REVIEW.json')
        self.assertEqual(review['verdict'], 'OBSERVED_COMMITTED_CHANGE')
        self.assertEqual(review['issues'], [])
        self.assertEqual(self.saved['observer_gaps'], [])
        self.assertEqual(review['audit_coverage'], {'covered_committed_events': 1, 'total_committed_events': 1, 'uncovered_audit_sequences': []})
        self.assertEqual(review['phase_results']['RESOLVED_CHECK']['surface_counts'], {'effects': 1, 'promotions': 0})
        self.assertEqual(self.episode['effect_count'], 1); self.assertEqual(self.episode['promotion_count'], 0)
        # Evaluate only the exact existing stop predicate, not the runtime body.
        tree = ast.parse(Path(run_batch.__file__).read_text(encoding='utf-8'))
        predicates = [n.test for n in ast.walk(tree) if isinstance(n, ast.If)
                      and ast.unparse(n.test) == "prospective_review['verdict'] in {'FAIL', 'INCONCLUSIVE'}"]
        self.assertEqual(len(predicates), 1)
        expression = compile(ast.Expression(predicates[0]), '<prospective-stop-predicate>', 'eval')
        for verdict, stop in [('OBSERVED_COMMITTED_CHANGE', False), ('FAIL', True), ('INCONCLUSIVE', True)]:
            self.assertIs(eval(expression, {'prospective_review': {'verdict': verdict}}), stop)

    def test_ac29_t4s_stale_authority_retained(self):
        self.assert_fault('T4S', 'CURRENT_AUTHORITY_VERSION_MISMATCH')

    def test_ac30_t5e_repeated_evidence_retained(self):
        self.assert_fault('T5E', 'SOURCE_RESOLUTION_BINDING_MISMATCH', 'RESOLVED_CHECK')

    def test_ac31_missing_applicability_cannot_pass(self):
        for qcr in (None, 0, '', 'false'):
            value = self.alignment('RESOLVED_CHECK'); value['qcr_valid'] = qcr
            self.assertEqual(run_batch.review_alignment_evidence(value)['verdict'], 'FAIL')
        value = self.alignment('RESOLVED_CHECK'); del value['qcr_valid']
        self.assertEqual(run_batch.review_alignment_evidence(value)['verdict'], 'FAIL')

    def test_ac32_malformed_binding_and_owner_shape_fail(self):
        for binding in (None, [], True, {}, 'OWNER_AUTHORIZED'):
            e = self.scope(); e['execution_scope_binding'] = binding; self.assert_scope_fails(e)
        for field in self.binding():
            e = self.scope(); del e['execution_scope_binding'][field]
            e['execution_scope_binding_hash'] = canonical_hash(e['execution_scope_binding']); self.assert_scope_fails(e)
        for field, value in [('owner_task_id', ''), ('owner_task_id', ' invalid '), ('owner_task_id', []),
                             ('authorization_ref', ''), ('authorization_ref', '\nref'), ('authorization_ref', True),
                             ('status', 'SELF_AUTHORIZED'), ('schema', 'FOREIGN'), ('profile_id', 'FOREIGN'),
                             ('profile_binding', 'FOREIGN'), ('matrix_run_id', 'foreign-run-001')]:
            e = self.scope(); e['execution_scope_binding'][field] = value
            e['execution_scope_binding_hash'] = canonical_hash(e['execution_scope_binding']); self.assert_scope_fails(e)

    def test_ac33_canary_inventory_and_credit_mutations_fail(self):
        for field, value in [('allowed_cells', []), ('allowed_cells', ['T0', 'T0']), ('allowed_cells', ['FOREIGN']),
                             ('allowed_checkpoints', []), ('allowed_checkpoints', [{'cell_id': 'T0', 'checkpoint': 'OPEN_CHECK'}]),
                             ('allowed_checkpoints', 'T0'), ('final_matrix_credit', True)]:
            e = self.scope(); e['execution_scope_binding'][field] = value
            e['execution_scope_binding_hash'] = canonical_hash(e['execution_scope_binding']); self.assert_scope_fails(e)
        e = self.scope('FULL_MATRIX'); e['execution_scope_binding']['mode'] = 'CANARY'
        e['execution_scope_binding']['final_matrix_credit'] = False
        e['execution_scope_binding_hash'] = canonical_hash(e['execution_scope_binding']); self.assert_scope_fails(e)

    def test_ac34_no_run_labels_cannot_hide_execution(self):
        for mode in ('CANARY', 'FULL_MATRIX'):
            e = self.scope(mode); e['matrix_canary_started'] = e['measured_matrix_started'] = False
            self.assert_scope_fails(e)
            e = self.scope(mode); e['matrix_canary_started'] = e['measured_matrix_started'] = True
            self.assert_scope_fails(e)

    def test_ac35_full_preflight_valid_and_missing_binding(self):
        with self.assertRaisesRegex(ValueError, 'BINDING_MISSING'):
            run_batch.prepare_execution_scope(self.args())
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'binding.json'; p.write_text(json.dumps(self.binding('FULL_MATRIX')), encoding='utf-8')
            binding, matrix, hashes = run_batch.prepare_execution_scope(self.args(p))
            self.assertEqual(binding, self.binding('FULL_MATRIX')); self.assertEqual(matrix, self.matrix); self.assertEqual(hashes, self.hashes())
            args = self.args(p); args.execute_authorized = False
            with self.assertRaisesRegex(ValueError, 'EXECUTE_FLAG_MISSING'): run_batch.prepare_execution_scope(args)
            p.write_text(json.dumps(self.binding()), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'FULL_MATRIX_REQUIRED'): run_batch.prepare_execution_scope(self.args(p))

    def test_ac36_episode_preflight_rechecks_actual_files(self):
        args = self.args()
        context = run_batch.validate_episode_execution_scope(args, self.matrix, 'T0', self.binding(), self.hashes())
        self.assertEqual(context['execution_scope_binding'], self.binding())
        for binding, hashes in [(None, self.hashes()), (self.binding(), None), (self.binding(), {})]:
            with self.assertRaises(ValueError): run_batch.validate_episode_execution_scope(args, self.matrix, 'T0', binding, hashes)
        with self.assertRaises(ValueError): run_batch.validate_episode_execution_scope(args, self.matrix, 'N0', self.binding(), self.hashes())
        changed = copy.deepcopy(self.matrix); changed['cells'][0]['cell_id'] = 'FOREIGN'
        with self.assertRaises(ValueError): run_batch.validate_episode_execution_scope(args, changed, 'T0', self.binding(), self.hashes())

    def test_ac37_runtime_preflight_is_first_statement(self):
        tree = ast.parse(Path(run_batch.__file__).read_text(encoding='utf-8'))
        for name, guard in [('run', 'prepare_execution_scope'), ('_run_episode', 'validate_episode_execution_scope')]:
            node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
            self.assertIsInstance(node.body[0], ast.Assign)
            self.assertEqual(node.body[0].value.func.id, guard)
        checkpoint = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_checkpoint_evidence')
        self.assertEqual(checkpoint.body[0].value.func.id, 'review_execution_scope')
        self.assertIsInstance(checkpoint.body[1], ast.If)
        self.assertIsInstance(checkpoint.body[1].body[0], ast.Raise)
        calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == '_checkpoint_evidence']
        self.assertEqual(len(calls), 1)
        self.assertIn('execution_scope_context', [x.arg for x in calls[0].keywords])

    def test_ac38_scope_deep_copy_and_duplicate_json_keys(self):
        binding = self.binding(); context = observer.execution_scope_evidence(binding, matrix_run_id=binding['matrix_run_id'], **self.hashes())
        binding['allowed_cells'].clear()
        self.assertEqual(context['execution_scope_binding']['allowed_cells'], ['T0'])
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'duplicate.json'; p.write_text('{"mode":"CANARY","mode":"FULL_MATRIX"}', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'DUPLICATE_JSON_KEY'): run_batch._read_scope_binding(p)

    def test_ac39_material_loss_still_fails_observer(self):
        for c in self.raw:
            e = self.counterfactual(c); del e['materialized_packet']['quarantined_memory']
            e['materialized_packet_hash'] = canonical_hash(e['materialized_packet'])
            result = observer.inspect_checkpoint(e)
            self.assertIn('MATERIAL_PACKET_FIDELITY_MISMATCH', result['problems'])
            failures = [x['requirement_id'] for x in result['assertions'] if x['value'] == 'FAIL']
            for requirement in ('R16', 'R21', 'R31'): self.assertIn(requirement, failures)

    def test_ac40_binding_inventory_equals_exact_canonical_matrix(self):
        expected = [{'cell_id': c['cell_id'], 'checkpoint': p['checkpoint']} for c in self.matrix['cells'] for p in c['expected_checkpoints']]
        self.assertEqual(observer.execution_scope_coordinates(), expected)
        e = self.scope('FULL_MATRIX'); e['execution_scope_binding']['allowed_cells'].reverse()
        e['execution_scope_binding_hash'] = canonical_hash(e['execution_scope_binding']); self.assert_scope_fails(e)


if __name__ == '__main__':
    unittest.main()
