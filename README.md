



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOBNMUKY%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T180922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIF2nwsThGfKnufc12j2l5W2RlVBYgjR1zg%2BO%2FqWXJ0XKAiEA15Bxk2%2BcjkW32DRcfrll9vX2M7HOS6JMT0wSs6uxyLoqiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMftnPriklsrmaGSSrcA8XlcoezPltHb59EEgXRz%2BursrGU8YIPj9GJYpxrpBzWAmsM%2FOhu1oHBJ5Ht12Xw%2BUpM867MRZkFlXvgjotQZav%2FoYKR6KTFlKIXUinds%2FJ0vBHWBnLDSxq2ZZ0ZUMD%2Fo9%2FvfmpqOYkEDAo6aYdMzhV%2B5wm%2BhkluJjaJpEx0XlvWss3mSP41MRJk6A2vPUBtWlhSXTNje4CMsCpXUo4FgEOxjdR2%2FZAYYWan0ZiRjsz%2Fd8cPljMOq7eVpDNZrpLMZlT%2FzWZMN%2FzQTFIdi60lG22krpXuhjIswUFlLXsyEzIjugXogsXc6DcgP26HpMEZmZ%2F0wVoBTLxo9J9v9IcutDkEAw9SHmY3qu9KamjFNNPPefdtOQv%2B5x%2F0vac11vcc6qCEowR6R11RjbDdDRlDvia%2Br6rC2ahOFyLiZ7OZT9MvrqVlGLGDvCy4%2Byoe7%2BoDFhuQzv2kMq1jy7xNYac5CNnQMDExY82RDknboKmlUHry%2Bg59qpgFS3oBiCli1rBGGG3X2OjLjCxpWX6MCEh%2FFwXW736qhFhH3rClsW9%2FLveopwt4WfY31gHpUzokikkNYJHmaarrP3APl8jo1S%2BSkpjq%2FFPTpxnu2UMDUWxVuk7k0zwOXOOXqIFqLRecMJHD2tUGOqUBPqjL1n90c%2BUMaUXqISw9rN36HMwtszh1gZ2sIAty0VaUR4tZCymRCPLg%2F9bJ52CSm3rPDjbZId4q2LSJay7fCv63KFnMt1pBoRUQ36T1AYOucMP9zVPdczP3pqrZhBksLEf%2FeBFc6t8QHdArwvm381kj512aygdg8fatu7dnfxFQjPI4XWXaFLLvymzw9R19b9tyOMlntkIRt%2BxOUL6lvOnZjjqE&X-Amz-Signature=f1ee373b81e9a195389dc32c4b5b6728933f3a257aeaa6d52f796b3b84038ac0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOBNMUKY%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T180922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIF2nwsThGfKnufc12j2l5W2RlVBYgjR1zg%2BO%2FqWXJ0XKAiEA15Bxk2%2BcjkW32DRcfrll9vX2M7HOS6JMT0wSs6uxyLoqiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMftnPriklsrmaGSSrcA8XlcoezPltHb59EEgXRz%2BursrGU8YIPj9GJYpxrpBzWAmsM%2FOhu1oHBJ5Ht12Xw%2BUpM867MRZkFlXvgjotQZav%2FoYKR6KTFlKIXUinds%2FJ0vBHWBnLDSxq2ZZ0ZUMD%2Fo9%2FvfmpqOYkEDAo6aYdMzhV%2B5wm%2BhkluJjaJpEx0XlvWss3mSP41MRJk6A2vPUBtWlhSXTNje4CMsCpXUo4FgEOxjdR2%2FZAYYWan0ZiRjsz%2Fd8cPljMOq7eVpDNZrpLMZlT%2FzWZMN%2FzQTFIdi60lG22krpXuhjIswUFlLXsyEzIjugXogsXc6DcgP26HpMEZmZ%2F0wVoBTLxo9J9v9IcutDkEAw9SHmY3qu9KamjFNNPPefdtOQv%2B5x%2F0vac11vcc6qCEowR6R11RjbDdDRlDvia%2Br6rC2ahOFyLiZ7OZT9MvrqVlGLGDvCy4%2Byoe7%2BoDFhuQzv2kMq1jy7xNYac5CNnQMDExY82RDknboKmlUHry%2Bg59qpgFS3oBiCli1rBGGG3X2OjLjCxpWX6MCEh%2FFwXW736qhFhH3rClsW9%2FLveopwt4WfY31gHpUzokikkNYJHmaarrP3APl8jo1S%2BSkpjq%2FFPTpxnu2UMDUWxVuk7k0zwOXOOXqIFqLRecMJHD2tUGOqUBPqjL1n90c%2BUMaUXqISw9rN36HMwtszh1gZ2sIAty0VaUR4tZCymRCPLg%2F9bJ52CSm3rPDjbZId4q2LSJay7fCv63KFnMt1pBoRUQ36T1AYOucMP9zVPdczP3pqrZhBksLEf%2FeBFc6t8QHdArwvm381kj512aygdg8fatu7dnfxFQjPI4XWXaFLLvymzw9R19b9tyOMlntkIRt%2BxOUL6lvOnZjjqE&X-Amz-Signature=3c6e5cf957dc4a450e9b8ea60605085bad5d5cb6e52fb8b5ad1d824b103dcd7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







