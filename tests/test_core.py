"""Unit tests for agent-dependency-license-sentinel."""
import unittest
from agent_dependency_license_sentinel.core import DependencyLicenseSentinel

class TestDependencyLicenseSentinel(unittest.TestCase):
    def test_permissive_pass(self):
        rep = DependencyLicenseSentinel.audit_dependencies(["requests", "flask"])
        self.assertTrue(rep.is_compliant)
        self.assertEqual(len(rep.violations), 0)

    def test_copyleft_taint(self):
        rep = DependencyLicenseSentinel.audit_dependencies(["requests", "gpl_module"])
        self.assertFalse(rep.is_compliant)
        self.assertTrue("VIRAL_COPYLEFT" in rep.violations[0])
