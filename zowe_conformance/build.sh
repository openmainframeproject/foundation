#!/bin/bash
#
# Builds the Zowe Conformance docs into pdfs
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#

cp brand_guidelines.pdf Zowe.Conformance.Program.-.Brand.Guidelines.pdf
pandoc participation_form.md -o Zowe.Conformance.Program.-.Participation.Form.pdf -f gfm --pdf-engine=wkhtmltopdf
pandoc terms_and_conditions.md -o Zowe.Conformance.Program.-.Terms.and.Conditions.pdf -f gfm --pdf-engine=wkhtmltopdf
pandoc test_evaluation_guide_table.md -f gfm --pdf-engine=wkhtmltopdf | wkhtmltopdf -O Landscape - Zowe.Conformance.Program.-.Test.Evaluation.Guide.Table.pdf
pandoc support_provider_evaluation_guide_table.md -f gfm --pdf-engine=wkhtmltopdf | wkhtmltopdf -O Landscape - Zowe.Support.Provider.-.Test.Evaluation.Guide.Table.pdf
