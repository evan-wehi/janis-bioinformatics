from abc import ABC
from datetime import datetime
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase

from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    File,
    Boolean,
    String,
    Int,
    Double,
    Float,
    InputSelector,
    Filename,
    ToolMetadata,
    InputDocumentation,
)


class GatkScatterIntervalsByNsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ScatterIntervalsByNs"

    def friendly_name(self) -> str:
        return "GATK4: ScatterIntervalsByNs"

    def tool(self) -> str:
        return "Gatk4ScatterIntervalsByNs"

    def inputs(self):
        return [
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output file for interval list. Required."
                ),
            ),
            ToolInput(
                tag="reference",
                input_type=File(optional=True),
                prefix="--REFERENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Reference sequence to use. Note: this tool requires that the reference fasta has both an associated index and a dictionary.  Required. "
                ),
            ),
            ToolInput(
                tag="arguments_file",
                input_type=File(optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="compression_level",
                input_type=Int(optional=True),
                prefix="--COMPRESSION_LEVEL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2."
                ),
            ),
            ToolInput(
                tag="create_index",
                input_type=Boolean(optional=True),
                prefix="--CREATE_INDEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create a BAM index when writing a coordinate-sorted BAM file. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="create_md5_file",
                input_type=Boolean(optional=True),
                prefix="--CREATE_MD5_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create an MD5 digest for any BAM or FASTQ files created. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="ga4gh_client_secrets",
                input_type=Boolean(optional=True),
                prefix="--GA4GH_CLIENT_SECRETS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: client_secrets.json."),
            ),
            ToolInput(
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 500000. "
                ),
            ),
            ToolInput(
                tag="max_to_merge",
                input_type=Int(optional=True),
                prefix="--MAX_TO_MERGE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-N) Maximal number of contiguous N bases to tolerate, thereby continuing the current ACGT interval.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="output_type",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_TYPE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OT) Type of intervals to output. Default value: BOTH. Possible values: {N, ACGT, BOTH}"
                ),
            ),
            ToolInput(
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tmp_dir",
                input_type=File(optional=True),
                prefix="--TMP_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more directories with space available to be used by this program for temporary storage of working files  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="use_jdk_deflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_DEFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_deflater)  Use the JDK Deflater instead of the Intel Deflater for writing compressed output  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="use_jdk_inflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_INFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_inflater)  Use the JDK Inflater instead of the Intel Inflater for reading compressed input  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="validation_stringency",
                input_type=Boolean(optional=True),
                prefix="--VALIDATION_STRINGENCY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Validation stringency for all SAM files read by this program.  Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: STRICT. Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--VERBOSITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Control verbosity of logging. Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
                ),
            ),
            ToolInput(
                tag="version",
                input_type=Boolean(optional=True),
                prefix="--version",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="display the version number for this tool Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="--showHidden",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-showHidden)  display hidden arguments  Default value: false. Possible values: {true, false} "
                ),
            ),
        ]

    def outputs(self):
        return []

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime.fromisoformat("2020-05-18T15:01:29.446711"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:01:29.446712"),
            documentation="b'USAGE: ScatterIntervalsByNs [arguments]\nWrites an interval list created by splitting a reference at Ns.A Program for breaking up a reference into intervals of\nalternating regions of N and ACGT bases.<br/><br/><br/>Used for creating a broken-up interval list that can be used for\nscattering a variant-calling pipeline in a way that will not cause problems at the edges of the intervals. By using\nlarge enough N blocks (so that the tools will not be able to anchor on both sides) we can be assured that the results of\nscattering and gathering the variants with the resulting interval list will be the same as calling with one large\nregion.\n<br/><h3>Input</h3>- A reference file to use for creating the intervals (needs to have index and dictionary next to it.)\n- Which type of intervals to emit in the output (Ns only, ACGT only or both.)\n- An integer indicating the largest number of Ns in a contiguous block that will be 'tolerated' and not converted into\nan N block.\n<h3>Output</h3>- An interval list (with a SAM header) where the names of the intervals are labeled (either N-block or\nACGT-block) to indicate what type of block they define.\n<h3>Usage example</h3><h4>Create an interval list of intervals that do not contain any N blocks for use with haplotype\ncaller on short reads</h4><pre>java -jar picard.jar ScatterIntervalsByNs \\\nREFERENCE=reference_sequence.fasta \\\nOUTPUT_TYPE=ACGT \\\nOUTPUT=output.interval_list\n</pre>\nVersion:4.1.3.0\n",
        )
