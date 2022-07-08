import json
import re
import subprocess


def check_infracost():
    """
    Check if infracost is installed
    """
    try:
        subprocess.check_output(["infracost", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False


def check_infracost_api_key():
    """
    Check if infracost API key is configured
    """
    try:
        subprocess.check_output(["infracost", "configure", "get", "api_key"])
        return True
    except subprocess.CalledProcessError:
        return False


def enable_infracost_dashboard():
    """
    Enable infracost dashboard
    """
    try:
        subprocess.check_output(
            ["infracost", "configure", "set", "enable_dashboard", "true"]
        )
        return True
    except subprocess.CalledProcessError:
        return False


def disable_infracost_dashboard():
    """
    Disable infracost dashboard
    """
    try:
        subprocess.check_output(
            ["infracost", "configure", "set", "enable_dashboard", "false"]
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_infracost_information(expression):
    process = subprocess.Popen(
        expression,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    data = json.loads(
        re.search("({.+})", stdout.decode("UTF-8"))
        .group(0)
        .replace("u'", '"')
        .replace("'", '"')
    )
    return data


def breakdown(path):
    """
    Run infracost on the given path and return the JSON output
    """
    try:
        infracost_data = get_infracost_information(
            ["infracost", "breakdown", "--path", path, "--format", "json"]
        )
        return infracost_data
    except subprocess.CalledProcessError:
        return None
    except AttributeError:
        return None


def diff(previous_path, new_path):
    try:
        infracost_diff = get_infracost_information(
            [
                "infracost",
                "diff",
                "--path",
                previous_path,
                "--compare-to",
                new_path,
                "--format",
                "json",
            ]
        )
        return infracost_diff
    except subprocess.CalledProcessError:
        return None
    except AttributeError:
        return None
