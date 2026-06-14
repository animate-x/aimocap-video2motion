# AIMoCap Workflow

AIMoCap is designed around motion delivery from short video.

## 1. Prepare a Source Clip

Use a clip with a clear subject, readable body motion, stable framing, and
minimal occlusion.

## 2. Trim the Useful Motion

Trim away idle frames before and after the motion segment. Shorter, cleaner
segments are easier to review.

## 3. Choose Output Targets

Current public targets:

- `default` for humanoid FBX output
- `unitree_g1` for robot motion JSON

## 4. Review and Download

Review generated motion before downloading output files for animation or robot
motion workflows.
