



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7SKHVML%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIFOnr7PxIf6kXynvCvgkp0FPhMCwG3cIw671FCARCp1BAiEAh27vGOWsf0A0KaATRUhlCLrQyPkHElyc98PWXKPBdtUq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMycWBuTA6fNK%2BdF%2FircA2ZiFu4jdyUJ9JF8JUWEOOOx8J6owt%2Bk7A7BbyRScpk1jLiVPYESrGGCCgkIqUEbCbIqDalMTVOOKdHmDCDg9jLuAski4OuIdrEYemb1BRg0LwaAx8qMohGCLJHkRaHw0nrJBCYX%2BuzLJN3U%2FJx2YXWq3lbEsvNX00sIsRARc3qNBwXksRWW2VuQn%2B%2FWQ0MJTTnCHBCIHTDjLvBKkcy4es6bSlZAJUhZ3OT178y1pQcDw%2BJ194bqsjrzWKWVZSXetYhpfLbtDaciqWqQj724HrvJATtQ5Y7Y8cG9dF8btNC9V6HoUWjwJnHKv9o37SMPI4WOwNugSSZ6YRo6k4xOvjUkLsmidXdJwnWWDUVZeUkuNyXXAk2Xb0gaBw7lZPwLo8f4Mej88Dtwq3yf19tT4PYihLMTsD1BIwJ%2FUGRGvievgBGV%2B5gPzz%2B4fz%2FFa9J71bvUoI1bx54z2%2BBB2gc2U0gFwxaS1wgcutyZs7apPZQ5dno6S7BWlUMsXDT%2BFlsiPeCA%2Fd7PUjhQEkVkVMAd%2FAjZ0DcjTF7eV%2F4ODye31ph4b3K%2FzxkvuGvkMKeIdwyYHM1s1aAPDVxpXUJ6pQ9nEMy%2B3DP80oVM3OCTqEyuArlrS6VFcSvT44EPlaA5MKrCrc4GOqUBg2c6y0YKi7LmqjiIT8U8l0clpRX8oRCClO5rtfJxzuA6Ae8hJN5uX%2FraIm0vwxjcxqdz8FQUlHj6RHESyUhdqN6RmGtz2xUiC%2BpskF5LfO0nIkfSFRK3oW1Pv7g1rnp3aO43iJxs3HKtrA1lMFYG7rFyXFGbp38P%2F%2FTvGT1JMho8Hkap08WaZ%2B1PHGHoIUSwNpltoQxKNIgJDSZeFVf%2F7USn4Mks&X-Amz-Signature=80fe6143264cc3e1e1d0a5ade484ca7cc4af983b17b142bbc9e7983899960cc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7SKHVML%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIFOnr7PxIf6kXynvCvgkp0FPhMCwG3cIw671FCARCp1BAiEAh27vGOWsf0A0KaATRUhlCLrQyPkHElyc98PWXKPBdtUq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMycWBuTA6fNK%2BdF%2FircA2ZiFu4jdyUJ9JF8JUWEOOOx8J6owt%2Bk7A7BbyRScpk1jLiVPYESrGGCCgkIqUEbCbIqDalMTVOOKdHmDCDg9jLuAski4OuIdrEYemb1BRg0LwaAx8qMohGCLJHkRaHw0nrJBCYX%2BuzLJN3U%2FJx2YXWq3lbEsvNX00sIsRARc3qNBwXksRWW2VuQn%2B%2FWQ0MJTTnCHBCIHTDjLvBKkcy4es6bSlZAJUhZ3OT178y1pQcDw%2BJ194bqsjrzWKWVZSXetYhpfLbtDaciqWqQj724HrvJATtQ5Y7Y8cG9dF8btNC9V6HoUWjwJnHKv9o37SMPI4WOwNugSSZ6YRo6k4xOvjUkLsmidXdJwnWWDUVZeUkuNyXXAk2Xb0gaBw7lZPwLo8f4Mej88Dtwq3yf19tT4PYihLMTsD1BIwJ%2FUGRGvievgBGV%2B5gPzz%2B4fz%2FFa9J71bvUoI1bx54z2%2BBB2gc2U0gFwxaS1wgcutyZs7apPZQ5dno6S7BWlUMsXDT%2BFlsiPeCA%2Fd7PUjhQEkVkVMAd%2FAjZ0DcjTF7eV%2F4ODye31ph4b3K%2FzxkvuGvkMKeIdwyYHM1s1aAPDVxpXUJ6pQ9nEMy%2B3DP80oVM3OCTqEyuArlrS6VFcSvT44EPlaA5MKrCrc4GOqUBg2c6y0YKi7LmqjiIT8U8l0clpRX8oRCClO5rtfJxzuA6Ae8hJN5uX%2FraIm0vwxjcxqdz8FQUlHj6RHESyUhdqN6RmGtz2xUiC%2BpskF5LfO0nIkfSFRK3oW1Pv7g1rnp3aO43iJxs3HKtrA1lMFYG7rFyXFGbp38P%2F%2FTvGT1JMho8Hkap08WaZ%2B1PHGHoIUSwNpltoQxKNIgJDSZeFVf%2F7USn4Mks&X-Amz-Signature=79b5311f987c95871e86d39671fb5eb5efbb41e3c81f31de8a84eb6b2a1f7e9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







