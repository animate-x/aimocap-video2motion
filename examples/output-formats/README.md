# Output Formats

AIMoCap currently focuses on two public output types.

## Humanoid FBX

The `default` target returns an FBX animation file for review, cleanup, and DCC
workflows such as Maya, MotionBuilder, Unity, or Unreal Engine.

## Unitree G1 Motion JSON

The `unitree_g1` target returns a robot motion JSON file.

Simplified shape:

```json
{
  "version": 1,
  "robotType": "unitree_g1",
  "fps": 30,
  "frameCount": 120,
  "root_pos": [[0.0, 0.0, 0.79]],
  "root_rot_xyzw": [[0.0, 0.0, 0.0, 1.0]],
  "dof_pos": [[0.0, 0.1, -0.2]]
}
```

The file represents per-frame robot base motion and joint positions.
