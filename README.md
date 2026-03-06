



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5AOMH4A%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T183705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIC0CSqPw69Ebj69NtoeSAsXizjFdR4kmak27lSHBty9zAiEA0hG68%2BeN1EMDnfLbPZoBHt6Vn9J0J1keEWh6dGOeeREqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKTHI6M8EetJBMQZircA2hcWjItaduvfny9F3IYSMH1f5fnD2FqEL%2FvzRekimAa3EWEo5dWgvrNPAzqHkoCOW%2FvxomN2vywC74%2B%2F2OxjaZBOxPsxUctKUMo8B4aRAH4l%2Bp1kSjsLv1qO%2BKQMC3SbLLOcoAYxH0LgQ2WrRvN%2B7OXZZfNQjYwpwjcadaQaigbAwpeAuuE3om7vvKibponeei%2FJFpWGS176tMv2nHabIP25Zu8b9pf6h3t0e8uCzs07V6kAplLOuBDgTiQ9boM3GmqRNDKSqgCFUKpW7MORuK9ZJyu3eyT4YeirFocFMfSFbBm3YnJBToQdeKz4D5RT%2F8oqXwPos4cVX11WdO2qn3HO0h7TI5p4oSYzCK1fDq8gmBiFgDA6qunuJYsa2%2FGN78m%2FwxVEVLhqs8wKfMt14INhBhrU5DEc3iZwInmoniqmNOI1qaJNSlW5G9Js9p%2FzTkPOPNswbMZeZtYZHiJpXX%2B651xESr0sYOhvAIulQ92vMyOMob%2Fyj%2FCBQ8s%2BY4So0Jf0zt0P5ErpznVJ0mBdcMM%2Bg0iqW9GUZg8WBPPrz8dnhoC6ucYnB46gzUSldL038%2Fr5kLf5XaneQaHl7LfZBbuWuT8fbl7kUejOwZfmmv0MjJJJiDhglAZkWaFMICfrM0GOqUBKkM%2BllfvJuAOVKKKp1jp71Kh5AlQnZtlQipqpB41emDY5Fn4bL52EeMo0PrSfoln3xDchlNQu2vJZdwa8T8%2FdSHtmyQWlPuo3yGyI1Xtnu3YkDApNKbFuXUO8vteBuCSwl4D6fP6Nqvz%2Fo9Q8e%2F26xJiCWECM9EwKc%2BN1kOuf8a4TTgKUcKGJrGtfMeEBG0r5IhB3N9VESbSW3JkntknlM2WWRba&X-Amz-Signature=c8ddaba456b3335e84c29eb08f8c877b4b41e7c0e4b805e1a3e50361bb8ae365&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5AOMH4A%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T183705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIC0CSqPw69Ebj69NtoeSAsXizjFdR4kmak27lSHBty9zAiEA0hG68%2BeN1EMDnfLbPZoBHt6Vn9J0J1keEWh6dGOeeREqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKTHI6M8EetJBMQZircA2hcWjItaduvfny9F3IYSMH1f5fnD2FqEL%2FvzRekimAa3EWEo5dWgvrNPAzqHkoCOW%2FvxomN2vywC74%2B%2F2OxjaZBOxPsxUctKUMo8B4aRAH4l%2Bp1kSjsLv1qO%2BKQMC3SbLLOcoAYxH0LgQ2WrRvN%2B7OXZZfNQjYwpwjcadaQaigbAwpeAuuE3om7vvKibponeei%2FJFpWGS176tMv2nHabIP25Zu8b9pf6h3t0e8uCzs07V6kAplLOuBDgTiQ9boM3GmqRNDKSqgCFUKpW7MORuK9ZJyu3eyT4YeirFocFMfSFbBm3YnJBToQdeKz4D5RT%2F8oqXwPos4cVX11WdO2qn3HO0h7TI5p4oSYzCK1fDq8gmBiFgDA6qunuJYsa2%2FGN78m%2FwxVEVLhqs8wKfMt14INhBhrU5DEc3iZwInmoniqmNOI1qaJNSlW5G9Js9p%2FzTkPOPNswbMZeZtYZHiJpXX%2B651xESr0sYOhvAIulQ92vMyOMob%2Fyj%2FCBQ8s%2BY4So0Jf0zt0P5ErpznVJ0mBdcMM%2Bg0iqW9GUZg8WBPPrz8dnhoC6ucYnB46gzUSldL038%2Fr5kLf5XaneQaHl7LfZBbuWuT8fbl7kUejOwZfmmv0MjJJJiDhglAZkWaFMICfrM0GOqUBKkM%2BllfvJuAOVKKKp1jp71Kh5AlQnZtlQipqpB41emDY5Fn4bL52EeMo0PrSfoln3xDchlNQu2vJZdwa8T8%2FdSHtmyQWlPuo3yGyI1Xtnu3YkDApNKbFuXUO8vteBuCSwl4D6fP6Nqvz%2Fo9Q8e%2F26xJiCWECM9EwKc%2BN1kOuf8a4TTgKUcKGJrGtfMeEBG0r5IhB3N9VESbSW3JkntknlM2WWRba&X-Amz-Signature=afd453c9ca74c6bcf2043ae660d518c459cf04e24fbc7dc19ebf66d6a061fad3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







