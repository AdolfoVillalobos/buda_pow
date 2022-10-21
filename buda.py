from src.proof_of_work import ProofOfWork
from src.utils import get_target, save_result

def summary(target, hashed, string):
    out = ""
    out += f"The target is: {target}\n"
    out += f"The string is: {string}\n"
    out += f"The hash is: {hashed}\n"
    return out

def main():
    num_repetitions = 1
    num_zeros = 2
    target = get_target(num_repetitions, num_zeros)

    pw = ProofOfWork()

    string, hashed = pw.do(target)
    save_result('results/proof_of_work.txt',
                summary(target, hashed, string))
    return

main()
