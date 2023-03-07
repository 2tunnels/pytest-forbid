from _pytest.pytester import Pytester


def test_requests_without_plugin(pytester: Pytester):
    pytester.copy_example("test_requests.py")

    result = pytester.runpytest()

    result.assert_outcomes(passed=1)


def test_requests_with_plugin(pytester: Pytester):
    pytester.copy_example("test_requests.py")

    result = pytester.runpytest("--forbid-requests")

    result.stdout.fnmatch_lines(["*forbid.exceptions.ForbiddenError*"])
    result.assert_outcomes(failed=1)
