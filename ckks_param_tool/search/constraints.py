class CKKSConstraints:
    def __init__(self, min_security_bits, max_error, max_runtime):
        self.min_security_bits = min_security_bits
        self.max_error = max_error
        self.max_runtime = max_runtime

    def is_feasible(self, params):
        return params.security_score >= self.min_security_bits

    def is_result_valid(self, result):
        return (
            result.error <= self.max_error and
            result.runtime <= self.max_runtime
        )
