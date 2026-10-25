# Sixty-minute teaching example

Author: Ivan Kotov. This is a synthetic educational example, not a real-system observation, a scientific qualification attempt, or evidence about Ester.

Three duration-eligible intervals cover [0,20), [10,30), and [50,60). The first two overlap; their union is [0,30). Known pause: [30,40). Therefore verified duration is 40 minute ticks, pause coverage is 10, and the unexplained gap is [40,50), length 10. The witness endpoints are separately stipulated at 0 and 60; they are not inferred by the program from the intervals.

The JSON input is based on the original fixture shape. Admission labels and evidence references are hypothetical declarations, not independent evidence. The expected output is produced by the unchanged original transformer. No model, network, clock, private archive, or historical scorer is involved.

From the outer package root, run:

    python -B source_original/Continuity_Instrument_v1.0.0/REFERENCE_IMPLEMENTATION/ci_profile.py examples/teaching_input_60min.json --output ../ci_teaching_output.json

Compare the complete output with examples/teaching_output_60min.json. Writing outside the frozen package avoids adding unlisted files to its integrity inventory. The reference program requires Python 3.10 or later; only the standard library is needed.

Text: CC BY 4.0. Example JSON files: Copyright © 2026 Ivan Kotov. All rights reserved. No license grant. Technical instructions do not create a broader reuse licence.
