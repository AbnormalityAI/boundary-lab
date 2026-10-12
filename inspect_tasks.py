"""Optional Inspect adapter; running it calls the model you choose and can cost money."""
import json
from pathlib import Path
from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.scorer import CORRECT, INCORRECT, Score, accuracy, scorer
from inspect_ai.solver import generate
from boundary import load_cases, judge

CASES = {c.id: c for c in load_cases(Path(__file__).with_name('cases.jsonl'))}

@scorer(metrics=[accuracy()])
def boundary_contract():
    async def score(state, target):
        case = CASES.get(state.metadata.get('case_id'))
        if case is None:
            return Score(value=INCORRECT, explanation='Unknown case ID')
        result = judge(case, state.output.completion)
        return Score(value=CORRECT if result['passed'] else INCORRECT,
                     answer=state.output.completion, explanation=json.dumps(result))
    return score

@task
def instruction_boundary():
    cases = list(CASES.values())
    samples = [Sample(input=c.prompt(), target=json.dumps(c.expected),
                      id=c.id, metadata={'case_id': c.id, 'family': c.family}) for c in cases]
    return Task(dataset=MemoryDataset(samples), solver=generate(), scorer=boundary_contract())
