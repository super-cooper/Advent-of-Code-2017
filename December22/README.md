# Sporifica Virus
Diagnostics indicate that the local __grid computing cluster__
has been contaminated with the __Sporifica Virus__. The grid
computing cluster is a seemingly-infinite two-dimensional
grid of compute nodes. Each node is either __clean__ or
__infected__ by the virus.

To
[prevent overloading](https://en.wikipedia.org/wiki/Morris_worm#The_Mistake)
the nodes (which would render them useless to the virus) or
detection by system administrators, exactly one __virus carrier__
moves through the network, infecting or cleaning nodes as it
moves. The virus carrier is always located on a single node
in the network (the __current node__) and keeps track of the
__direction__ it is facing.

To avoid detection, the virus carrier works in bursts; in
each burst, it __wakes up__, does some __work__, and goes
back to __sleep__. The following steps are all executed __in
order__ one time each burst:

 - If the __current node__ is __infected__, it turns to its
 __right__. Otherwise, it turns to its __left__. (Turning is
 done in-place; the __current node__ does not change.)
 - If the __current node__ is __clean__, it becomes __infected__.
 Otherwise, it becomes __cleaned__. (This is done after the
 node is considered for the purposes of changing direction.)
 - The virus carrier
 [moves](https://www.youtube.com/watch?v=2vj37yeQQHg) __forward__
 one node in the direction it is facing.

Diagnostics have also provided a __map of the node infection
status__ (your puzzle input). __Clean__ nodes are shown as `.`;
infected nodes are shown as `#`. This map only shows the
center of the grid; there are many more nodes beyond those
shown, but none of them are currently infected.

The virus carrier begins in the middle of the map facing __up__.

For example, suppose you are given a map like this:

```
..#
#..
...
```

Then, the middle of the infinite grid looks like this, with
the virus carrier's position marked with `[ ]`:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

The virus carrier is on a __clean__ node, so it turns __left__,
__infects__ the node, and moves left:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]# . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

The virus carrier is on an __infected__ node, so it turns
__right__, __cleans__ the node, and moves up:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . . # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

Four times in a row, the virus carrier finds a __clean__,
__infects__ it, turns __left__, and moves forward,
ending in the same place and still facing up:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . #[#]. # . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

Now on the same node as before, it sees an infection,
which causes it to turn __right__, __clean__ the node, and
move forward:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . # .[.]# . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

After the above actions, a total of `7` bursts of activity
had taken place. Of them, `5` bursts of activity caused an
infection.

After a total of `70`, the grid looks like this, with the
virus carrier facing up:

```
. . . . . # # . .
. . . . # . . # .
. . . # . . . . #
. . # . #[.]. . #
. . # . # . . # .
. . . . . # # . .
. . . . . . . . .
. . . . . . . . .
```

By this time, `41` bursts of activity caused an infection
(though most of those nodes have since been cleaned).

After a total of `10000` bursts of activity, `5587` bursts
will have caused an infection.

Given your actual map, after `10000` bursts of activity,
__how many bursts cause a node to become infected__?
(Do not count nodes that begin infected.)

Your puzzle answer was `5322`.

## Part Two
As you go to remove the virus from the infected nodes, it
__evolves__ to resist your attempt.

Now, before it infects a clean node, it will __weaken__ it to
disable your defenses. If it encounters an infected node, it
will instead __flag__ the node to be cleaned in the future. So:

 - __Clean__ nodes become __weakened__.
 - __Weakened__ nodes become __infected__.
 - __Infected__ nodes become __flagged__.
 - __Flagged__ nodes become __clean__.

Every node is always in exactly one of the above states.

The virus carrier still functions in a similar way, but now
uses the following logic during its bursts of action:

 - Decide which way to turn based on the __current node__:
    - If it is __clean__, it turns __left__.
    - If it is __weakened__, it does __not__ turn, and will
    continue moving in the same direction.
    - If it is __infected__, it turns __right__.
    - If it is __flagged__, it __reverses__ direction, and
    will go back the way it came.
 - Modify the state of the __current node__, as described above.
 - The virus carrier moves __forward__ one node in the
 direction it is facing.

Start with the same map (still using `.` for __clean__ and `#`
for infected) and still with the virus carrier starting in
the middle and facing __up__.

Using the same initial state as the previous example, and
drawing __weakened__ as `W` and __flagged__ as `F`, the
middle of the infinite grid looks like this, with the
virus carrier's position again marked with `[ ]`:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

This is the same as before, since no initial nodes are
__weakened__ or __flagged__. The virus carrier is on a
clean node, so it still turns left, instead __weakens__ the
node, and moves left:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

The virus carrier is on an infected node, so it still turns
right, instead __flags__ the node, and moves up:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . F W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

This process repeats three more times, ending on the
previously-flagged node and facing right:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
. . W[F]W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

Finding a flagged node, it reverses direction and __cleans__
the node:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
. .[W]. W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

The __weakened__ node becomes infected, and it continues in
the same direction:

```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
.[.]# . W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

Of the first `100` bursts, `26` will result in __infection__.
Unfortunately, another feature of this evolved virus is __speed__;
of the first `10000000` bursts, `2511944` will result in
__infection__.

Given your actual map, after `10000000` bursts of activity,
__how many bursts cause a node to become infected__?
(Do not count nodes that begin infected.)

Your puzzle answer was `2512079`.