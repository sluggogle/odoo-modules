from openerp import models, fields, api
from openerp.tools.translate import _
import os
import logging

_logger = logging.getLogger(__name__)


#####################################
#
# Update
#
####################################
class ReportLabel(models.Model):
    _inherit = 'report'

    def _build_wkhtmltopdf_args(self, paperformat, specific_paperformat_args=None):
        """Build arguments understandable by wkhtmltopdf from a report.paperformat record.

        :paperformat: report.paperformat record
        :specific_paperformat_args: a dict containing prioritized wkhtmltopdf arguments
        :returns: list of string representing the wkhtmltopdf arguments
        """
        command_args = []
        if paperformat.id == 3:
            command_args.extend(['--disable-smart-shrinking'])

        if paperformat.format and paperformat.format != 'custom':
            command_args.extend(['--page-size', str(paperformat.format)])

        if paperformat.page_height and paperformat.page_width and paperformat.format == 'custom':
            command_args.extend(['--page-width', str(paperformat.page_width) + 'mm'])
            command_args.extend(['--page-height', str(paperformat.page_height) + 'mm'])

        command_args.extend(['--margin-left', str(paperformat.margin_left)])
        command_args.extend(['--margin-right', str(paperformat.margin_right)])

        if specific_paperformat_args and specific_paperformat_args.get('data-report-margin-top'):
            command_args.extend(['--margin-top', str(specific_paperformat_args['data-report-margin-top'])])
        else:
            command_args.extend(['--margin-top', str(paperformat.margin_top)])

        command_args.extend(['--margin-bottom', str(paperformat.margin_bottom)])

        if specific_paperformat_args and specific_paperformat_args.get('data-report-dpi'):
            command_args.extend(['--dpi', str(specific_paperformat_args['data-report-dpi'])])
        elif paperformat.dpi:
            if os.name == 'nt' and int(paperformat.dpi) <= 95:
                _logger.info("Generating PDF on Windows platform require DPI >= 96. Using 96 instead.")
                command_args.extend(['--dpi', '96'])
            else:
                command_args.extend(['--dpi', str(paperformat.dpi)])

        if specific_paperformat_args and specific_paperformat_args.get('data-report-header-spacing'):
            command_args.extend(['--header-spacing', str(specific_paperformat_args['data-report-header-spacing'])])
        elif paperformat.header_spacing:
            command_args.extend(['--header-spacing', str(paperformat.header_spacing)])

        if paperformat.orientation:
            command_args.extend(['--orientation', str(paperformat.orientation)])
        if paperformat.header_line:
            command_args.extend(['--header-line'])

        _logger.info('WKHTMLTOPDF: %s', command_args)
        return command_args
