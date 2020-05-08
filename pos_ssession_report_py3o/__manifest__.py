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
    'name': "pos session report py3o",
    'version': '12.0.1',
    'summary': """""",
    'description': """report for pos session Py3o """,
    'author': "Ahmed Mnasri",
    'website': "",
    'category': 'Point Of Sale',
    'depends': [
        'base',
		'report_py3o',
		'point_of_sale', 
            ],
    'data': [
        
        'report/report.xml',
    ],
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}

