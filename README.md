



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMCRKFJ3%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T123334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDHoGRDt6Dno7PWon6awgHsQCBJxTOk2OMLccJ0cfLExgIgQgb7rydrJt%2F%2BSIAdff7IZOmvD%2BiqX%2FPbQFTe31I%2BoJIqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJHyO0m8t4dUlR%2FA1SrcA%2BwISKroR%2FWIFekHS8aN6kSSWfVt3ITB4fJS%2B7ilXQDm%2FPI%2BhXHd08QDZIZFTWbwLdHJCtF0Rb25ynk%2Fq%2BtD%2FRUYq7uM2FBIvkzgU2TM%2BATOGcXEUaDTKKxorR2lbnrYwJQSFa463mCOQxSTlE9Tw3JMlDEMj5IxV7QejyMkT2lNX86SHRkfi5jUG4VVBm4baXP7j2AAZVmKWPfRDx2qg66J1n0ys%2FwIuyVx8YHWc99pDOeXH4%2FdsT078ylsTIFgbLzQskkFIPlVmPY1JUYiIMACmf4ico%2Ft4ap7wmi86Rq%2BUgb5gZiON2hIlodR9IND46n2bmFcvd72Iuk183rnP17kyzSuxDmImzR7MnYdkJ%2F81jPTdPC77tgtweBKrvbW0bC1eCPdlmfp2vD9X2PqIHeK0w3KzN8l7WGXpnBUxKeNj%2BqkQOn4Xrf%2F8bCpd3OpvMsTBgvFz18%2Fuf20wQs57i76AhMFAnw8HECV%2FAvOJ2kDbeMnMYtqemNBar%2BUU8yzchaef%2BkJav5VLDT4k65itEl6nEJmKRiQih3v0t7X%2B7%2FrvM0%2FtRqh9DoamEdcC2dweMkMVttIU%2FbPFZPe2gJGm5m0%2BQjnF%2BI7pAJuy%2FuY9KyEP%2FM10bspOAqFM6iCMOm42MoGOqUBNGkNv0rh1rh5dJT1mdUQkfMXG%2FaWBH9aD5YaXcRYp7WkD8OCBtGhYVl1nRtyy%2BeO57XwJKb8NMvDsfOlbKsTtoRHOnxa2%2FFcpYkl%2BN31ySbtMuhigt8QoQPRaxhuKCnWXxjqzh8sMGbsc%2F4CCoWQTTFAO5vf5lsbdin%2FDzHpN0mydJZD0cPrwtPfHNIC3P2qmmeWIT175bYKaUz5P98ptyS1xB3d&X-Amz-Signature=5367bc10fd64f330664fcf1d552c275808a9fc72fad3302c2bd50a9515feb1b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMCRKFJ3%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T123334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDHoGRDt6Dno7PWon6awgHsQCBJxTOk2OMLccJ0cfLExgIgQgb7rydrJt%2F%2BSIAdff7IZOmvD%2BiqX%2FPbQFTe31I%2BoJIqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJHyO0m8t4dUlR%2FA1SrcA%2BwISKroR%2FWIFekHS8aN6kSSWfVt3ITB4fJS%2B7ilXQDm%2FPI%2BhXHd08QDZIZFTWbwLdHJCtF0Rb25ynk%2Fq%2BtD%2FRUYq7uM2FBIvkzgU2TM%2BATOGcXEUaDTKKxorR2lbnrYwJQSFa463mCOQxSTlE9Tw3JMlDEMj5IxV7QejyMkT2lNX86SHRkfi5jUG4VVBm4baXP7j2AAZVmKWPfRDx2qg66J1n0ys%2FwIuyVx8YHWc99pDOeXH4%2FdsT078ylsTIFgbLzQskkFIPlVmPY1JUYiIMACmf4ico%2Ft4ap7wmi86Rq%2BUgb5gZiON2hIlodR9IND46n2bmFcvd72Iuk183rnP17kyzSuxDmImzR7MnYdkJ%2F81jPTdPC77tgtweBKrvbW0bC1eCPdlmfp2vD9X2PqIHeK0w3KzN8l7WGXpnBUxKeNj%2BqkQOn4Xrf%2F8bCpd3OpvMsTBgvFz18%2Fuf20wQs57i76AhMFAnw8HECV%2FAvOJ2kDbeMnMYtqemNBar%2BUU8yzchaef%2BkJav5VLDT4k65itEl6nEJmKRiQih3v0t7X%2B7%2FrvM0%2FtRqh9DoamEdcC2dweMkMVttIU%2FbPFZPe2gJGm5m0%2BQjnF%2BI7pAJuy%2FuY9KyEP%2FM10bspOAqFM6iCMOm42MoGOqUBNGkNv0rh1rh5dJT1mdUQkfMXG%2FaWBH9aD5YaXcRYp7WkD8OCBtGhYVl1nRtyy%2BeO57XwJKb8NMvDsfOlbKsTtoRHOnxa2%2FFcpYkl%2BN31ySbtMuhigt8QoQPRaxhuKCnWXxjqzh8sMGbsc%2F4CCoWQTTFAO5vf5lsbdin%2FDzHpN0mydJZD0cPrwtPfHNIC3P2qmmeWIT175bYKaUz5P98ptyS1xB3d&X-Amz-Signature=1d9bd7234dfa1fad4fb56042ae878458fc945c7eadfa1a90863a89ea480d86bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







