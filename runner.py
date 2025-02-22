import os
import subprocess
from pathlib import Path
import time
import platform

from BasePage.logger import Logger

logger = Logger("runner").get_log()


def run_pytest(allure_results_dir: Path):
    """
    运行 pytest 并生成 allure 结果。
    :param allure_results_dir: 存储 pytest allure 结果的目录
    """
    full_path = os.path.abspath('../playwright-Binzhouxiaofang/TestCases/TestLogin.py')
    command = ['pytest', full_path, f'--alluredir={allure_results_dir}']
    logger.info(f"Running pytest with command: {command}")
    try:
        result = subprocess.run(command, check=False, text=True, capture_output=True, encoding='utf-8')

        logger.info(result.stdout)
        if result.stderr:
            logger.error(f"pytest stderr: {result.stderr}")
        if result.returncode != 0:
            logger.warning(f"pytest exited with return code {result.returncode}")
    except Exception as e:
        logger.error(f"An error occurred while running pytest: {e}")
        raise


def generate_allure_report(allure_results_dir: Path, html_report_dir: Path):
    """
    生成 Allure 报告。
    :param allure_results_dir: 存储 pytest allure 结果的目录
    :param html_report_dir: 生成的 HTML 报告目录
    """
    current_dir = Path(__file__).resolve().parent
    allure_dir = current_dir.parent / 'playwright-Binzhouxiaofang' / 'Utils' / 'allure-2.30.0'
    # 根据操作系统选择 Allure 命令
    allure_cmd_name = 'allure.bat' if platform.system() == 'Windows' else 'allure'
    allure_cmd = allure_dir / 'bin' / allure_cmd_name

    if not allure_cmd.exists():
        logger.error(f"Allure executable not found at {allure_cmd}")
        raise FileNotFoundError(f"Allure executable not found at {allure_cmd}")

    command = [str(allure_cmd), 'generate', str(allure_results_dir), '-o', str(html_report_dir), '--clean']
    logger.info(f"Generating Allure report with command: {command}")

    try:
        result = subprocess.run(
            command,
            check=True,
            text=True,
            capture_output=True
        )
        logger.info(result.stdout)
        logger.info(f"Allure report generated at: {html_report_dir}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error generating Allure report: {e.stderr}")
        raise


def open_allure_report(report_dir: Path):
    """
    打开生成的 Allure 报告。
    :param report_dir: 生成的 HTML 报告目录
    """
    current_dir = Path(__file__).resolve().parent
    allure_dir = current_dir.parent / 'playwright-Binzhouxiaofang' / 'Utils' / 'allure-2.30.0'
    allure_cmd_name = 'allure.bat' if platform.system() == 'Windows' else 'allure'
    allure_cmd = allure_dir / 'bin' / allure_cmd_name

    if not allure_cmd.exists():
        logger.error(f"Allure executable not found at {allure_cmd}")
        raise FileNotFoundError(f"Allure executable not found at {allure_cmd}")

    command = [str(allure_cmd), 'open', str(report_dir)]
    logger.info(f"Opening Allure report with command: {command}")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error opening Allure report: {e}")
        logger.error(f"Return code: {e.returncode}")
        logger.error(f"Output: {e.stdout}")
        logger.error(f"Error output: {e.stderr}")
        raise


def generate_report():
    """
    生成测试报告的主方法，调用 run_pytest 和 generate_allure_report 方法。
    """
    # 获取当前时间，并定义报告的文件名和路径
    now = time.strftime("%Y%m%d%H%M", time.localtime())
    base_dir = Path(__file__).resolve().parent / 'TestReport'
    allure_results_dir = base_dir / f'allure_results_{now}'
    html_report_dir = base_dir / f'html_report_{now}'

    # 创建报告目录（如果不存在）
    allure_results_dir.mkdir(parents=True, exist_ok=True)
    html_report_dir.mkdir(parents=True, exist_ok=True)

    try:
        run_pytest(allure_results_dir)
        generate_allure_report(allure_results_dir, html_report_dir)
        open_allure_report(html_report_dir)  # 打开报告
    except Exception as e:
        logger.error(f"报告生成失败: {e}")


if __name__ == "__main__":
    generate_report()
