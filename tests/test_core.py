from eval_dashboard.core import Run, summarize
def test_mean_score(): assert summarize([Run("x",[.2,.8],1,0,1)])[0]["mean_score"] == .5
