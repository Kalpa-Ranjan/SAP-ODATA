



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZJ6LYT7%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T070837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIA%2BI5mxmDFgX6FXz93yNc20ozDPq2yVSmVw0LxFkaTWGAiEApdKSeFrungPThapHn5lSKwwKkU566Wr8PYo1gV5ItWgqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOh1UxldbIqkncMzaSrcA6vOrRCuAK3vJCloLpFC2rBCObiDRY6kPdFYEfAGQzSmOIWWWzv3gvF870oYSAp%2FTN9MVe9jbFBA0fbZnX0IdCmAxiu73f11WeUgqwQhw2pxE9mjscpZdiEl5Ou4lLyDi8Cid2kHNgPbTS6k42YNfjR1UiH2wRjeIYGdntaZ2HLCWCgJvBhR2C1aNtZ8VS0MhlMeCykcSDVQ0MUAypoPwkPO7P5NHU1AhYpw74dVdFBzv9j%2FQNQUkHGXiQIpbngfpI6eq%2BS8aP3hk%2FtLPIyICcrXXDSCXrL0oNVacBs%2FhjBWd2pAeCr%2BDzFfzsbJY5lwUGuhyGpWZAQHn671%2BF7KE%2Fwh%2FlKYr8%2FTOWUajHc8g90IUAx7pY14alLfDuVi1EMGxbuYMlVPBgAZHf0aLYX6j7LfH6y8NVtfSAiA%2BWDFwlISRFGX3fvi2vjVYxSu8ckxtcaz9dMv1LH1MuBB3CHsoPoJj2F98LMz2WVy6q85TM1sXT%2FirA9xTdoQLqCrKwK8rLi%2Fr6LMD0Up%2FgfVC4CbToJ%2BOoLlja4%2BzAPVOgi1k5VZhSRmcWJPV8ASbKi3wtuWNeqiIfZZQOK7%2B4TGeXgMXYL6P608%2F3IDzb1Q%2FA86%2FQvq0pXSdl7Ecl8%2FFJ%2FTMILO0s4GOqUBGc8GHqFCQgHSwtr9QH2pnXPBP9wXrNaIOMR0g7YItQOKrS2B91YhwWByulk4udhZur94izPb5DCvmYPmJcCrq2lhs6PAMmVx4x03JndZT7ihOCHzKmnKAAG%2BEsklXTrdXVG3Vk6e%2B6eSAI%2B8p4mP8H4E9QSeSFrG%2ByiyfyKgle3Zgr1pELTL8lAJxyQzpACqw4khwx88AsztjqqcIrsGBu97z5jr&X-Amz-Signature=bf8a0eaf42f44971ea8e70f64dc4cb55054e6ca13e10894be8c426d0348b3bfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZJ6LYT7%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T070837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIA%2BI5mxmDFgX6FXz93yNc20ozDPq2yVSmVw0LxFkaTWGAiEApdKSeFrungPThapHn5lSKwwKkU566Wr8PYo1gV5ItWgqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOh1UxldbIqkncMzaSrcA6vOrRCuAK3vJCloLpFC2rBCObiDRY6kPdFYEfAGQzSmOIWWWzv3gvF870oYSAp%2FTN9MVe9jbFBA0fbZnX0IdCmAxiu73f11WeUgqwQhw2pxE9mjscpZdiEl5Ou4lLyDi8Cid2kHNgPbTS6k42YNfjR1UiH2wRjeIYGdntaZ2HLCWCgJvBhR2C1aNtZ8VS0MhlMeCykcSDVQ0MUAypoPwkPO7P5NHU1AhYpw74dVdFBzv9j%2FQNQUkHGXiQIpbngfpI6eq%2BS8aP3hk%2FtLPIyICcrXXDSCXrL0oNVacBs%2FhjBWd2pAeCr%2BDzFfzsbJY5lwUGuhyGpWZAQHn671%2BF7KE%2Fwh%2FlKYr8%2FTOWUajHc8g90IUAx7pY14alLfDuVi1EMGxbuYMlVPBgAZHf0aLYX6j7LfH6y8NVtfSAiA%2BWDFwlISRFGX3fvi2vjVYxSu8ckxtcaz9dMv1LH1MuBB3CHsoPoJj2F98LMz2WVy6q85TM1sXT%2FirA9xTdoQLqCrKwK8rLi%2Fr6LMD0Up%2FgfVC4CbToJ%2BOoLlja4%2BzAPVOgi1k5VZhSRmcWJPV8ASbKi3wtuWNeqiIfZZQOK7%2B4TGeXgMXYL6P608%2F3IDzb1Q%2FA86%2FQvq0pXSdl7Ecl8%2FFJ%2FTMILO0s4GOqUBGc8GHqFCQgHSwtr9QH2pnXPBP9wXrNaIOMR0g7YItQOKrS2B91YhwWByulk4udhZur94izPb5DCvmYPmJcCrq2lhs6PAMmVx4x03JndZT7ihOCHzKmnKAAG%2BEsklXTrdXVG3Vk6e%2B6eSAI%2B8p4mP8H4E9QSeSFrG%2ByiyfyKgle3Zgr1pELTL8lAJxyQzpACqw4khwx88AsztjqqcIrsGBu97z5jr&X-Amz-Signature=a519c059de0eb262453ed6b0bd6dd52ea81058225c9cae5f4268b4de84496b0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







