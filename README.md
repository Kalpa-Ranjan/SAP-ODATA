



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT2GMNA6%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T201251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCICA%2Fsqtv3OJhRYPnYtpby7pwC%2BxRrsxMC87VZJ63%2FGX4AiEAzOV3HYSdX6hTNksw9XMc9JkbWB2ZHkrq9MYZMHtpTaIqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOjLa6LuW35ycbudUSrcA1JW6Klk1TkrPZtcjZ%2BRXnJkoIauEXpV1adL23ziCoApPr2zpU84s%2BziDS1N4OLF95wV2Fw0qf5ehINyc%2BA%2BzO9wPf3m%2FbW%2FiaDQShtlwLA0%2Bam6UST6tc96oHwtsWH4feeCxZMDhK3kZWzyABnW874DbmjGTQ8wVtJZ3cJjWJuZTOVj%2B6OevTt9tzI3kRxkpNWAHXVn%2BZVClEiDaLJDEMh82by8WaifgyXcZh6CPuuxUIepUdmKOC%2FthEv4nT0NnMctV97y8qTJeO2zwEu3S8oXmO86iCbvWRmySWBRqjBAMsGHfxhvBVBApBjno5OC0YC%2Fd6SvkXE56H94PVO0OKyybKpIbrHWHjjEIkiDKmxa7eZnazNbYWFHXveLyBiKievmy5TCBPHa4yBtNNL8UMrVrfNdZn1M%2BBISql0Vqy0N%2BwzMHUvbdQxrikmoXpuOhRumYDqB2dvQXNVeA6I40SN90CFYHYn3iHiwhXWJ9Lb8IUk3ctZcuVFNJASx8S2OYSzQZoWqntT6itwjNHZTsDRArVMerBYiqWzTzEHz00RC0SG46BXIGJHdjJTlc3JhuUrDkUXBG%2BSf3tVpPOIUa2zRkbN0WEBy1oiadszQYCL0%2F1RCiKbZzX0YnJgQMPPe59AGOqUB5O8f7By8LVP3Zgjh%2BcVOpAj5lezCOesXcxaN9yPtUFeIYYc4P9ko60VBcYRvGjJSlBFMYbPJiBH064h93YzUeQ3dIOiMIKuyb737QTVXFPL%2BKaw9cZrHvqJgWOnHkfE4wNHAxhPqw%2FHwO%2FA4F%2BgrIpb2eIq5%2FU77vGEgfe2iE6OdRTQLS63aznbObM84MsXaiNkScbSeabwggiJoEzTpY7wDULCT&X-Amz-Signature=4bddd26900c54b5e6e813b00594af53deba80a85b969a1a385e9f4ad17c7a1b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT2GMNA6%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T201251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCICA%2Fsqtv3OJhRYPnYtpby7pwC%2BxRrsxMC87VZJ63%2FGX4AiEAzOV3HYSdX6hTNksw9XMc9JkbWB2ZHkrq9MYZMHtpTaIqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOjLa6LuW35ycbudUSrcA1JW6Klk1TkrPZtcjZ%2BRXnJkoIauEXpV1adL23ziCoApPr2zpU84s%2BziDS1N4OLF95wV2Fw0qf5ehINyc%2BA%2BzO9wPf3m%2FbW%2FiaDQShtlwLA0%2Bam6UST6tc96oHwtsWH4feeCxZMDhK3kZWzyABnW874DbmjGTQ8wVtJZ3cJjWJuZTOVj%2B6OevTt9tzI3kRxkpNWAHXVn%2BZVClEiDaLJDEMh82by8WaifgyXcZh6CPuuxUIepUdmKOC%2FthEv4nT0NnMctV97y8qTJeO2zwEu3S8oXmO86iCbvWRmySWBRqjBAMsGHfxhvBVBApBjno5OC0YC%2Fd6SvkXE56H94PVO0OKyybKpIbrHWHjjEIkiDKmxa7eZnazNbYWFHXveLyBiKievmy5TCBPHa4yBtNNL8UMrVrfNdZn1M%2BBISql0Vqy0N%2BwzMHUvbdQxrikmoXpuOhRumYDqB2dvQXNVeA6I40SN90CFYHYn3iHiwhXWJ9Lb8IUk3ctZcuVFNJASx8S2OYSzQZoWqntT6itwjNHZTsDRArVMerBYiqWzTzEHz00RC0SG46BXIGJHdjJTlc3JhuUrDkUXBG%2BSf3tVpPOIUa2zRkbN0WEBy1oiadszQYCL0%2F1RCiKbZzX0YnJgQMPPe59AGOqUB5O8f7By8LVP3Zgjh%2BcVOpAj5lezCOesXcxaN9yPtUFeIYYc4P9ko60VBcYRvGjJSlBFMYbPJiBH064h93YzUeQ3dIOiMIKuyb737QTVXFPL%2BKaw9cZrHvqJgWOnHkfE4wNHAxhPqw%2FHwO%2FA4F%2BgrIpb2eIq5%2FU77vGEgfe2iE6OdRTQLS63aznbObM84MsXaiNkScbSeabwggiJoEzTpY7wDULCT&X-Amz-Signature=f2781c6daa2e0750760a51e95683df5f933bb24916a7727d4a923be420a285be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







