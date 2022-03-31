#!/bin/bash
#
# Builds the Zowe V2 Conformance docs into pdfs
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#

pandoc zowe_apiml_test_evaluation_guide_v2.md -f gfm --pdf-engine=wkhtmltopdf | wkhtmltopdf - zowe_apiml_test_evaluation_guide_v2.pdf
pandoc zowe_app_framework_test_evaluation_guide_v2.md -f gfm --pdf-engine=wkhtmltopdf | wkhtmltopdf - zowe_app_framework_test_evaluation_guide_v2.pdf
pandoc zowe_cli_test_evalution_guide_v2.md -f gfm --pdf-engine=wkhtmltopdf | wkhtmltopdf - zowe_cli_test_evalution_guide_v2.pdf
pandoc zowe_explorer_test_evaluation_guide_v2.md -f gfm --pdf-engine=wkhtmltopdf | wkhtmltopdf - zowe_explorer_test_evaluation_guide_v2.pdf
pandoc zowe_support_provider_test_evaluation_guide_v2.md -f gfm --pdf-engine=wkhtmltopdf | wkhtmltopdf - zowe_support_provider_test_evaluation_guide_v2.pdf
