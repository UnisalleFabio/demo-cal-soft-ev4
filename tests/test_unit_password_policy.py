import unittest

from _helpers import ROOT  # noqa: F401
from virtual_campus.password_policy import PasswordPolicy, PasswordPolicyError


class PasswordPolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = PasswordPolicy(min_length=10)

    def test_accepts_a_strong_password(self) -> None:
        self.policy.validate("ClaveSegura123!")

    def test_rejects_password_without_uppercase(self) -> None:
        with self.assertRaises(PasswordPolicyError):
            self.policy.validate("clavesegura123!")

    def test_rejects_password_without_special_character(self) -> None:
        with self.assertRaises(PasswordPolicyError):
            self.policy.validate("ClaveSegura123")


if __name__ == "__main__":
    unittest.main()
