
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()


def start_scheduler(job_function, interval_minutes=60):
    """Start automated report scheduling."""

    if scheduler.running:
        logger.info("Scheduler is already running.")
        return

    scheduler.add_job(
        job_function,
        trigger="interval",
        minutes=interval_minutes,
        id="automated_report_job",
        replace_existing=True
    )

    scheduler.start()
    logger.info("Scheduler started successfully.")


def stop_scheduler():
    """Stop the background scheduler."""

    if scheduler.running:
        scheduler.shutdown(wait=False)
        logger.info("Scheduler stopped.")
      
