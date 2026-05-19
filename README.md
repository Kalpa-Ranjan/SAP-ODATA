



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z5J5RKO%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T093333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIE4wHTBteSo%2F3JTh91Fw%2F1unP7MGXLpQS9wHHoI0a%2BB5AiA41MxpPfI8eZxkJQ9KaMfTMfcZ0trTpoH5laRyme2jtiqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJLhj6ZOOs1LVzQhAKtwDKoX8CZNLv6LKSynGY9v5b7%2BpKD%2BHU8iU%2BEeT%2BpP2HF3SClf93KFOu%2FcZUEQ0JwfTbl6Z%2BOF6DExudRlZ4uOCowYc%2BHDIf9MIwInUebd8RWQTUx7dUQWbQVnAbmIAaEX71%2FsTLH5uN5ew2KNbKnQKkwSxnGJet8xOXS5jo9uKcKXxhTTV0cVnMkF3305%2BxL7FjhuzSgap5cRHW7dVR2%2F88dQTmdlX6EAnemjQTGHW0W0tgcBLOPf13sm6gDFa%2BykYdsoaQ8HAxrnE9f5K7hKj8KyD%2FgL9AZUVaJ%2FuNmnOKL7PZn3MMujRZ1ucqzpdGvJtalfLSjrkZQaZ0b4lM3bUTx1fXG6MMDlWRo8XmGI2Hbe640bFelo7Mpj5EqAqp6vZkYpkNAuD%2BgruPlc%2BGMeye4rLQI5iTzTJhdUOwJnr5NfV02kSd%2FzfMhW38ILs6ptTlIjAKcwZkoSnYIOa4FH7y5wZ6hUxeUY5OHHZRpksZFoWt7L6wyCsl84VwJQsgplHDb3E9gytzWKSq64EIgPWetxCD0DkiO%2FIdSo6MvuQbE6b64GSOrw1j%2Fsc3F1nwtsfEz8VfrmScz9KiMowz8V%2BF0xJ4sb%2BTlCbkEpgB1gf4ijVihGrGUFJkfJzgDcw3dGw0AY6pgH8fNlv8nv7P2gG4s3T6qAWq3e1%2B1xOcK00FUbtd1k65cbZ1XuD2oeFQ8nZW81QLegIxwFiTa4WoEdIiuSnUq44Xe4d%2BQk2Evxh22gSfnZxVCl6rkWApmts4F85hXQxUhWBxNVav%2Bt0829tN%2BZ4Fx3nm1szjh6dhNgUiBOCrrB8kx9l8DAKcueKRv9jvAQNH%2BU1SbG0Cms8e1FpMcuDTxFzKtgxL4Oz&X-Amz-Signature=92271eb5a1ec2771054df260c405103037b1588f83f5d9f7e50188704295f71b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z5J5RKO%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T093334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIE4wHTBteSo%2F3JTh91Fw%2F1unP7MGXLpQS9wHHoI0a%2BB5AiA41MxpPfI8eZxkJQ9KaMfTMfcZ0trTpoH5laRyme2jtiqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJLhj6ZOOs1LVzQhAKtwDKoX8CZNLv6LKSynGY9v5b7%2BpKD%2BHU8iU%2BEeT%2BpP2HF3SClf93KFOu%2FcZUEQ0JwfTbl6Z%2BOF6DExudRlZ4uOCowYc%2BHDIf9MIwInUebd8RWQTUx7dUQWbQVnAbmIAaEX71%2FsTLH5uN5ew2KNbKnQKkwSxnGJet8xOXS5jo9uKcKXxhTTV0cVnMkF3305%2BxL7FjhuzSgap5cRHW7dVR2%2F88dQTmdlX6EAnemjQTGHW0W0tgcBLOPf13sm6gDFa%2BykYdsoaQ8HAxrnE9f5K7hKj8KyD%2FgL9AZUVaJ%2FuNmnOKL7PZn3MMujRZ1ucqzpdGvJtalfLSjrkZQaZ0b4lM3bUTx1fXG6MMDlWRo8XmGI2Hbe640bFelo7Mpj5EqAqp6vZkYpkNAuD%2BgruPlc%2BGMeye4rLQI5iTzTJhdUOwJnr5NfV02kSd%2FzfMhW38ILs6ptTlIjAKcwZkoSnYIOa4FH7y5wZ6hUxeUY5OHHZRpksZFoWt7L6wyCsl84VwJQsgplHDb3E9gytzWKSq64EIgPWetxCD0DkiO%2FIdSo6MvuQbE6b64GSOrw1j%2Fsc3F1nwtsfEz8VfrmScz9KiMowz8V%2BF0xJ4sb%2BTlCbkEpgB1gf4ijVihGrGUFJkfJzgDcw3dGw0AY6pgH8fNlv8nv7P2gG4s3T6qAWq3e1%2B1xOcK00FUbtd1k65cbZ1XuD2oeFQ8nZW81QLegIxwFiTa4WoEdIiuSnUq44Xe4d%2BQk2Evxh22gSfnZxVCl6rkWApmts4F85hXQxUhWBxNVav%2Bt0829tN%2BZ4Fx3nm1szjh6dhNgUiBOCrrB8kx9l8DAKcueKRv9jvAQNH%2BU1SbG0Cms8e1FpMcuDTxFzKtgxL4Oz&X-Amz-Signature=b53f9c4c6a07b1da78cf0ce9721ec265de78bc7fe2dd3516c332b15aad8215de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







