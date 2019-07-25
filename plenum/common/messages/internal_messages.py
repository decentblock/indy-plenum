from typing import NamedTuple, List, Any

from plenum.common.messages.node_messages import CheckpointState, PrePrepare

ValidatorsChanged = NamedTuple('ValidatorsChange',
                               [('names', List[str])])

LegacyViewChangeStatusUpdate = NamedTuple('StartViewChange',
                                          [('in_progress', bool)])

ParticipatingStatus = NamedTuple('LedgerParticipatingStatus',
                                 [('is_participating', bool)])

HookMessage = NamedTuple('HookMessage',
                         [('hook', int),
                          ('args', tuple)])

OutboxMessage = NamedTuple('OutboxMessage',
                           [('msg', Any)])

DoCheckpointMessage = NamedTuple('DoCheckpoinitMessage',
                                 [('state', CheckpointState),
                                  ('start_no', int),
                                  ('end_no', int),
                                  ('ledger_id', int),
                                  ('view_no', int)])

RemoveStashedCheckpoints = NamedTuple('RemoveStashedCheckpoints',
                                      [('start_no', int),
                                       ('end_no', int),
                                       ('view_no', int),
                                       ('all', bool)])

RequestPropagates = NamedTuple('RequestPropagates',
                               [('bad_requests', List)])

NodeModeMsg = NamedTuple('NodeModeMsg',
                         [('mode', int)])

PrimariesBatchNeeded = NamedTuple('PrimariesBatchNeeded',
                                  [('pbn', bool)])

CurrentPrimaries = NamedTuple('CurrentPrimaries',
                              [('primaries', list)])

TryOrderMsg = NamedTuple('TryOrderMsg',
                         [('inst_id', int),
                          ('key', tuple),
                          ('pp', PrePrepare)])
