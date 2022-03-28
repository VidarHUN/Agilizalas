# Agilizalas

Link to venv:
https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde


## Specification

### Task

The task is to retrieve messages from a network log. There are messages going between
several components that are worth identifying which relationship there is. Events have been
recorded, which contain the details of the messages. Part of the task is to extract the
parameter keys from the messages and then make a visual sequence diagram representation
based on the information available.

### Message structure in order

1. Timestamp
2. Sender component
3. Event
4. Originator (Which port is running)
5. Operation (send/receive)
6. Receiver component
7. Message type (function)
8. Keys (Body of the message)

### Further information

#### Event types

We only have inspect two kind of events:

- **PORTEVENT**: This is the message
- **TIMEROP**: This is a timer

The TIMEROP is a special message that addresses itself and it has
three types:

- start
- stop
- timeout

### Requirements

1. Separate each events
2. Identify of the type of events
3. Identify the sender and receiver component
4. Filter out the important events
5. Filter out the important events' required fields (keys, type of the timer)
6. Visual representation

## Git branching strategy

- Use feature branches for all new features and bug fixes.
- Merge feature branches into the main branch using pull requests.
- Keep a high quality, up-to-date main branch.

Name the feaute branches like this:

- feature/description
- bugfix/description

Please review every PR before merging it. 

[link](https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops)

Also for commiting:

- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Use the body to explain what and why vs. how

[link](https://cbea.ms/git-commit/)
