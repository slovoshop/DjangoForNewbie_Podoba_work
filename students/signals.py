
# -*- coding: utf-8 -*-

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models.students import Student
from .models.groups import Group

import logging

@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
	"""Writes information about newly added or updated student into \
	log file"""
	logger = logging.getLogger(__name__)

	student = kwargs['instance']

	if kwargs['created']:
		logger.info("Student added: %s %s (ID: %d)", student.first_name,
		student.last_name, student.id)
	else:
		logger.info("Student updated: %s %s (ID: %d)", student.first_name,
		student.last_name, student.id)



@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
	"""Writes information about deleted student into log file"""
	logger = logging.getLogger(__name__)

	student = kwargs['instance']

	logger.info("Student deleted: %s %s (ID: %d)", student.first_name,
	student.last_name, student.id)


@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
	"""Writes information about newly added or updated student into \
	log file"""
	logger = logging.getLogger(__name__)

	group = kwargs['instance']

	if kwargs['created']:
		logger.info("Group added: %s, leader - %s (ID: %d)", group.title,
		group.leader, group.id)
	else:
		logger.info("Group updated: %s, leader - %s (ID: %d)", group.title,
		group.leader, group.id)


