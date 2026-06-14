# AIMoCap Workflow

AIMoCap is designed around motion delivery from short video. The recommended
workflow keeps input clips short, target selection explicit, and review steps
visible before downloading files.

## 1. Prepare a Source Clip

Use a clip with:

- one clearly visible subject
- stable framing
- readable full-body motion
- limited occlusion
- a short duration focused on the action

## 2. Trim the Useful Motion

Trim away idle frames before and after the motion segment. Shorter, cleaner
segments are easier to inspect and compare across output targets.

## 3. Choose Output Targets

Current public targets:

| Target ID | Output | Review Goal |
| --- | --- | --- |
| `default` | FBX | Check character animation transfer |
| `unitree_g1` | motion JSON | Check robot-oriented motion sequence |

## 4. Inspect Preview Output

Review visual output before downloading files. This step is useful for detecting
source issues such as partial occlusion, camera cuts, or ambiguous body motion.

## 5. Download and Validate

Download target-specific files only after preview review. Animation outputs
should be checked in the downstream DCC or engine workflow. Robot-oriented
motion outputs should be validated in simulation or another controlled review
environment before further use.
