import math

def calculate_entropy(probabilities):
    """
    Calculate the entropy given a list of probabilities.
    
    :param probabilities: List of probabilities for each outcome
    :return: Entropy in bits
    """
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def entropy_standard_die():
    """Calculate entropy for a standard 6-sided die."""
    probabilities = [1/6] * 6
    entropy = calculate_entropy(probabilities)
    print(f"Entropy for standard die: {entropy*5:.4f} bits")

def entropy_modified_die():
    """Calculate entropy for the modified die (1,2,3,4,5,5)."""
    probabilities = [1/6, 1/6, 1/6, 1/6, 1/3]
    entropy = calculate_entropy(probabilities)
    print(f"Entropy for modified die: {entropy:.4f} bits")

if __name__ == "__main__":
    entropy_standard_die()
    entropy_modified_die()