# Seeker

Seeker is a novel co-design approach that leverages and extends coresets to efficiently execute DNN inference across a set of EH sensor nodes and a host mobile device. Seeker focuses on building an efficient EH-WSN which can collaboratively work to maximize the inferences performed at the EH-edge nodes.  Furthermore, it then applies innovative coreset techniques to efficiently and intelligently offload unfinished compute tasks to a more capable host to further increase the inferences that can be performed.

To the best of our knowledge, Seeker is the first work to propose task-aware coreset computation}and coreset recovery. Further, Seeker integrates coresets with commercial energy harvesting systems}along with proposing emerging hardware solutions to perform maximum computation at the edge. The proposed coreset construction and recovery can also be generalized to different data modalities.

Following is the block diagram of Seeker:
![ResearchDiagrams-Page-3](https://user-images.githubusercontent.com/15208196/236058165-f3106e1a-f6ff-432d-9f75-3310df393f4c.jpg)

Seeker ecosystem includes both a sensor-array and a host. The goal is to maximize the compute at the edge and communicate the leftover compute in an efficient way to the host to finish. Seeker uses the following decision process to xecute its entire workflow:

![ResearchDiagrams-Page-4](https://user-images.githubusercontent.com/15208196/236057904-cac02977-f4cf-41f6-9bd4-8ed9d8154ebd.jpg)
