# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright.
#    Author: Ahmed Mnasri
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Invoice report py3o",
    'version': '12.0.1',
    'summary': """""",
    'description': """Invoice template Py3o """,
    'author': "Ahmed Mnasri",
    'website': "",
    'category': 'account',
    'depends': [
        'account',
		'report_py3o',
		'timbre_fiscal',
        'report_py3o_fusion_server', 
        'base_usability',  
            ],
    'data': [
        'report/report.xml',
        'views/num_to_word_view.xml',
    ],
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}

