# Seeker

Seeker is a novel co-design approach that leverages and extends coresets to efficiently execute DNN inference across a set of EH sensor nodes and a host mobile device. Seeker focuses on building an efficient EH-WSN which can collaboratively work to maximize the inferences performed at the EH-edge nodes.  Furthermore, it then applies innovative coreset techniques to efficiently and intelligently offload unfinished compute tasks to a more capable host to further increase the inferences that can be performed.

To the best of our knowledge, Seeker is the first work to propose task-aware coreset computation}and coreset recovery. Further, Seeker integrates coresets with commercial energy harvesting systems}along with proposing emerging hardware solutions to perform maximum computation at the edge. The proposed coreset construction and recovery can also be generalized to different data modalities.

Following is the block diagram of Seeker:

![ResearchDiagrams-Page-3](https://user-images.githubusercontent.com/15208196/236058165-f3106e1a-f6ff-432d-9f75-3310df393f4c.jpg)

Seeker ecosystem includes both a sensor-array and a host. The goal is to maximize the compute at the edge and communicate the leftover compute in an efficient way to the host to finish. Seeker uses the following decision process to xecute its entire workflow:

![ResearchDiagrams-Page-4](https://user-images.githubusercontent.com/15208196/236057904-cac02977-f4cf-41f6-9bd4-8ed9d8154ebd.jpg)

_**Task Aware Coreset Construction**_
Seeker, instead of perfroming a naïve coreset construction, adapts to the task. That means, constructing elaborate coresets for complex tasks and and simpler ones for simple tasks. Seeker leverages the temporal locality to do the same. Following figure shows the communication benifits of using task aware coresets:

![image](https://user-images.githubusercontent.com/15208196/236060899-02b1670c-1c3a-4435-a4c2-d3e054ea6831.png)

_**Coreset Recovery:**_
At the host, depending on the coreset constuction algorithm, a recovery is performed. Seeker used two different recovery mechanism (as shown in figure below) to do the same. 

<img width="700" alt="image" src="https://user-images.githubusercontent.com/15208196/236059628-ab91d4b4-f002-4ffc-b72a-a921bd60ce57.png">

_**Seeker on Commercial Hardware**_
Coreset has been deployed on multiple hardware platforms including nRF52840 and MSP-EXP430FR5994 (with Llow energy accelerator) with Pixel 6 Pro as the host device. We have also tested Seeker for predictive maintenance. We developed a dataset (released in the repository: [Seeker-MachineStatus](https://github.com/TheSeekerProject/Seeker-MachineStatus))

![image](https://user-images.githubusercontent.com/15208196/236062322-ce86b8aa-f813-464a-96a3-cf6e88f72542.png)
