# coding: utf8
# Copyright (c) 2022, excle and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import csv
from frappe.core.doctype.file.file import File


class AccountMigration(Document):

    def before_save(self, *args, **kwargs):

        file = self.get_file(self.file_data)

        file_path = self.build_file_path(file)

        print(file_path)

        with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            for row in csv_reader:
                self.create_account(row)

    def get_file(self, file_url: str) -> File:

        try:
            file_name = frappe.get_list(
                "File",
                filters={"file_url": file_url})[0]['name']
            file = frappe.get_doc("File", file_name)
            return file
        except Exception as e:
            frappe.log_error(frappe.get_traceback(),
                             f'The Error is: {e}')
            return None

    def build_file_path(self, file: File) -> str:
        local_site_path = frappe.utils.get_site_path()
        file_type = 'private' if file.is_private else 'public'
        file_path = file.file_url if \
            file_type == 'private' else f'/public{file.file_url}'
        return f'{local_site_path}{file_path}'

    def create_account(self, account_data: dict):

        print(len(account_data['account_number']))

        return
