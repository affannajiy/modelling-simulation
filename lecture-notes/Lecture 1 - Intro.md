---
title: Lecture 1 - Intro and ABM
type: lecture
course: Modelling and Simulation
lecture: 1
date: 2026-09-14
publish: true
tags: [mns, abm, des, simulation, netlogo]
---

<!--
Cornell method (Pauk, "How to Study in College"):
  Record  - during lecture, fill the Notes column. Short phrases, abbreviations, examples.
  Reduce  - within 24h, write cues in the left column: questions, keywords, prompts.
            Turn each block of notes into a question - Who / What / When / Where / Why / How
            (5W1H). If a block yields no question, it is probably not worth keeping.
  Recite  - hide the Notes column, answer each cue aloud from memory.
            Feynman check: could you explain this answer to a friend outside the course?
            If not, the gap goes in Reflection.
  Reflect - add your own connections / questions under Reflection.
  Review  - re-read weekly; keep the Summary to 3-5 sentences.
  Sources - name + link, nothing else: slides, textbook chapter, papers the lecturer cited.
            No files in the vault; it is all online anyway.
  Related - link every idea that deserves its own note: [[Topics]], [[Companies]], [[Media]].
            Links are what make the graph useful; folders and tags do not.
-->

## Notes

| Cues                                                         | Notes                                                                                                                                                                                                                                                                                |
| :----------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| What is a simulation?                                        | Imitation of the dynamics of a real-world process. Replaces the real thing so we can study cause and effect without touching it.                                                                                                                                                     |
| What is a model?                                             | A description of the real thing. Made of: logical process, mathematical relations, statistical description based on parameters. Eg F = ma describes motion but ignores everything else (friction, drag). Model = the description, simulation = running it to imitate the real stuff. |
| What is a system?                                            | Collection of entities that interact with each other towards a goal. Eg crowd behaviour in a stadium during an emergency, or a bank queue and how to improve the queueing process.                                                                                                   |
| Data science vs simulation - what is the difference?         | Data science focuses on the result (what will happen). Simulation focuses on the process (why it happens and how it evolves over time).                                                                                                                                              |
| Final exam entry process - what are the steps?               | 1. Students arrive and wait. 2. Security opens door. 3. Security checks students. 4. Students search for their table.                                                                                                                                                                |
| Final exam entry - what questions would a simulation answer? | How long until everyone settles? When should students be let in? How to balance two concerns: start on time vs not letting students in too early? How to improve the process?                                                                                                        |
| Why does precision management need simulation?               | Precise, real-time data needed. Eg Mecca hajj stampede killed many people; Saudi gov then used simulation to improve crowd control.                                                                                                                                                  |
| How is a simulation actually built?                          | Formulas and equations executed step by step. Write pseudocode first, then implement in NetLogo.                                                                                                                                                                                     |
| What is the course project about?                            | Drones, AUVs, robot swarms. Autonomous aerial drones moving together with poor sensing, limited power, weak network connectivity. Also autonomous car swarming. Multidisciplinary by nature: physics, robotics, maths.                                                               |
| ABM vs DES - how do they differ?                             | Same problem, two approaches, results will not match but they complement each other. **ABM** (agent-based): each agent acts on its own based on the path laid out, the environment, and other agents. **DES** (discrete event): driven by statistics and probability of events.      |

## Reflection

- The F = ma example is a good reminder that a model is always a simplification. The question is whether the stuff left out matters for what I am trying to answer.
- Exam entry and hajj crowd control are the same problem at different scales: people, a bottleneck, and a timing decision. Worth trying the exam one in NetLogo as a first ABM.
- Why would ABM and DES give different results for the same system? Guess: ABM lets behaviour emerge from local rules, DES assumes distributions up front. Ask in class.

## Summary

Simulation imitates a real process so I can study cause and effect without the real thing. A model is the description (logic, maths, statistics) and a simulation is that model running over time. Unlike data science, which predicts the result, simulation explains the process. This course builds simulations in NetLogo from pseudocode, using either agent-based (ABM) or discrete event (DES) approaches, which are complementary, and the project is on drone and robot swarms.

## Sources

- Slides: Lecture 1 - Intro and ABM (course slides)
- Reading:

## Related

- [[Agent-Based Modelling]]
- [[Discrete Event Simulation]]
- [[NetLogo]]

If we have a thought experiment, we think of what happens when everyone goes out and buy stuff at the same time now. Would it require simulation?

- Yes we would like to require the simulation because we want to have a more convincing case of the thought experiment.

We are trying to understand reality by applying simulation

The model does not match the real world. The model is an abstrction, and its just a simplication of the thing in the real world. Its just made up of description, logic process, and mathematical formula.

Static Model, time does not play a role of the actualy. For example, a model of a bridge testing its stability.

Dynamic Model, is the model changes over time

Discrete, it means that its not continuous. Continuous models variables of interest change continuously over time.

An operation in the factory, we would like to simulate the process of loading and unloading the stuff from a truck. We can model this and this would be a discrete independant event. Because one guy unloading the truck, one guy loading the truck using a forklift, then a guy loading the warehouse.

Continuous model usually involves the Partial Differential Equation. We simulate the physics of the real world. For example, a leaf falling on the ground, the wind blowing at our face. In simulation, theres a particle based simulation which every fluid particle has their own behaviour but still involved as the same group.

Simulation is multidisciplinary, we an use computer science to do the software but we need to have the mathematics behind it. Then maybe we would talk to biologist and physicist. It would still be cheaper to run in a simulation than rather making the real experiment in real world.
