# Zowe Conformance Program materials

This contains the following materials relevant to the Zowe Conformance Program:

- [Test Evaluation Guide table](/test_evaluation_guide_table.md)
- [Terms and Conditions](terms_and_conditions.md)
- [Participation Form](participation_form.md)
- [Brand Guidelines](brand_guidelines.pdf)
- [Test Evaluation Guide](test_evaluation_guide.md) - deprecated

The documents are the source versions; final version are made available on the [Zowe Conformance Program page](https://www.openmainframeproject.org/projects/zowe/conformance).

## Build instructions

Converting the markdown to PDF can be achieved leveraging [pandoc](https://pandoc.org/) and [wkhtmltopdf](https://wkhtmltopdf.org/) as shown below for releases.

```bash
cp brand_guidelines.pdf Zowe.Conformance.Program.-.Brand.Guidelines.pdf
pandoc participation_form.md -o Zowe.Conformance.Program.-.Participation.Form.pdf -f gfm --pdf-engine=wkhtmltopdf
pandoc terms_and_conditions.md -o Zowe.Conformance.Program.-.Terms.and.Conditions.pdf -f gfm --pdf-engine=wkhtmltopdf
pandoc test_evaluation_guide.md -o Zowe.Conformance.Program.-.Test.Evaluation.Guide.pdf -f gfm --pdf-engine=wkhtmltopdf
pandoc test_evaluation_guide_table.md -o Zowe.Conformance.Program.-.Test.Evaluation.Guide.Table.pdf -f gfm --pdf-engine=wkhtmltopdf
```
