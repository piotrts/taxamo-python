#!/usr/bin/env python
"""
Copyright 2014 Taxamo, Ltd.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Input_transaction:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'invoice_date': 'str',
            'invoice_address': 'invoice_address',
            'buyer_credit_card_prefix': 'str',
            'custom_fields': 'list[custom_fields]',
            'additional_currencies': 'additional_currencies',
            'buyer_tax_number': 'str',
            'custom_id': 'str',
            'tax_country_code': 'str',
            'force_country_code': 'str',
            'buyer_email': 'str',
            'original_transaction_key': 'str',
            'buyer_ip': 'str',
            'invoice_place': 'str',
            'verification_token': 'str',
            'tax_deducted': 'bool',
            'buyer_name': 'str',
            'evidence': 'evidence',
            'custom_data': 'str',
            'billing_country_code': 'str',
            'invoice_number': 'str',
            'currency_code': 'str',
            'description': 'str',
            'supply_date': 'str',
            'transaction_lines': 'list[input_transaction_line]',
            'order_date': 'str'

        }


        #Invoice date of issue.
        self.invoice_date = None # str
        #Invoice address.
        self.invoice_address = None # invoice_address
        #Buyer's credit card prefix.
        self.buyer_credit_card_prefix = None # str
        #Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers.
        self.custom_fields = None # list[custom_fields]
        #Additional currency information - can be used to receive additional information about invoice in another currency.
        self.additional_currencies = None # additional_currencies
        # Buyer's tax number - EU VAT number for example.
        self.buyer_tax_number = None # str
        #Custom identifier provided upon transaction creation.
        self.custom_id = None # str
        #Two-letter ISO country code, e.g. FR. This code applies to detected/set country for transaction, but can be set using manual mode.
        self.tax_country_code = None # str
        #Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.
        self.force_country_code = None # str
        #Buyer's declared email address.
        self.buyer_email = None # str
        #Use data and evidence from original transaction. Tax will be re-calculated, but evidence won't be re-checked.
        self.original_transaction_key = None # str
        #IP address of the buyer in dotted decimal (IPv4) or text format (IPv6).
        self.buyer_ip = None # str
        #Invoice place of issue.
        self.invoice_place = None # str
        #Verification token
        self.verification_token = None # str
        #True if the transaction deducted from tax and no tax is applied. Either set automatically when VAT number validates with VIES correctly, but can also be provided in manual mode.
        self.tax_deducted = None # bool
        #Buyer's name - first name and last name or company name.
        self.buyer_name = None # str
        #Tax country of residence evidence.
        self.evidence = None # evidence
        #Custom data related to transaction.
        self.custom_data = None # str
        #Billing two letter ISO country code.
        self.billing_country_code = None # str
        #Invoice number.
        self.invoice_number = None # str
        #Currency code for transaction - e.g. EUR.
        self.currency_code = None # str
        #Transaction description.
        self.description = None # str
        #Supply date in yyyy-MM-dd format.
        self.supply_date = None # str
        #Transaction lines.
        self.transaction_lines = None # list[input_transaction_line]
        #Order date in yyyy-MM-dd format.
        self.order_date = None # str
        
