from dataclasses import dataclass, asdict
import statistics
@dataclass
class Run: model: str; scores: list[float]; latency_ms: float; cost_usd: float; safety_pass_rate: float
def summarize(runs: list[Run]) -> list[dict]:
    out=[]
    for r in runs:
        x=asdict(r); x["mean_score"]=statistics.mean(r.scores); out.append(x)
    return sorted(out, key=lambda x:x["mean_score"], reverse=True)
