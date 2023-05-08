# Copyright (c) 2023, abdul basit  and contributors
# For license information, please see license.txt

import frappe
from frappe import _,throw


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	conditions = get_conditions(filters)
	data = get_data(conditions)
	return columns, data

def get_data(conditions): 
	data  = frappe.db.sql("""
		SELECT 
			si.name as sales_invoice,
			si.token,
			tok.issue_date,
			si.customer
		FROM
		 `tabToken`  tok inner join `tabSales Invoice`  si on si.name = tok.name
		WHERE
		si.token is Not Null {0}
	""".format(conditions),as_dict=1)



	return data


def get_conditions(filters):
	conditions = ""
	
	if filters.get('from_date'):
		conditions += " and posting_date >=  '{}'".format(filters.get('from_date'))
	if filters.get('to_date'):
		conditions += " and posting_date <= '{}'".format(filters.get('to_date'))

	return conditions



def get_columns():
	columns = [
	{
			'fieldname': 'link_sales_invoices',
			'label': _("Linked Sales Invoice"),
			'fieldtype': 'Link',
			"options": "Sales Invoice",
			"width": "230",
		},
		{
			'fieldname': 'Token',
			'label': "Token",
			'fieldtype': 'Data',
			
			"width": "120",
		},
		{
			'fieldname': 'issued_date',
			'label': _("Issued Date"),
			'fieldtype': 'Date',
			"width": "150",
		},
		{
			'fieldname': 'customer',
			'label': _("Customer"),
			'fieldtype': 'Link',
			"options": "Customer",
			'width': '120'
		},
		
	]

	return columns