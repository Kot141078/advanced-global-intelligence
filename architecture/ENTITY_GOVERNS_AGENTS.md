# Entity-centered orchestration: `c` governs agents

## Rule
By default, `c` orchestrates agents; agents do not define `c`.

## Meaning
In this stack, agents are subordinate processes and tools. They may call models, retrieve context, execute bounded tasks, or act as specialized workers. They do not hold the primary continuity of the system.

## What holds continuity
Continuity belongs to `c`, not to any single model, worker, judge, or swarm. Model replacement, tool replacement, or worker rotation does not by itself redefine the entity.

## Human role
`a` remains the accountable human anchor. Human intent, responsibility, and escalation authority do not disappear into the swarm. `c` carries this intent through complexity and time.

## Why agents exist
Agents are useful where task complexity exceeds direct human handling. They expand operational variety, but only under explicit privilege, bounded scope, auditable invocation, and stopping conditions governed by `c`.

## Non-goal
This is not an agent-first architecture. A swarm without `c` is not the subject of the system. It is an execution surface.

## Relation to L4
L4 constraints still apply: identity, auditable privileges, budgets, oracle scarcity, irreversibility, and fail-closed behavior. `c` is the layer that must hold these constraints while coordinating subordinate agents.
