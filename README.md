



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5Y5TWCJ%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T062147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCW3ilGxNT8AvVccwgW4JcN7hhgXmyJbzYsHFZOY0NtQgIgErLCUc2NNs0GoOoMqrFB00Pj%2F6IJqjVxfi7qsH5ldhcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLU%2FgHmNYAZkf7Ko%2BircA7VhHqb8q8h9tiYPlffbBOsHVQtHGhTbIFf03F%2FcB2RFM%2F5jOsCr1uqQXI0sD5m%2FeixaescsDLg4mINzm8xKGoKwTcJMIXRIqEo12aTys6klv5RE5ywAbk8TpZv72dME78y6KnOil8KSYPXfGmoATWg1xYW6je36ZOaoRcgtwPhFTSpvJS%2FiU32FeR5LOZnmz2n%2Fx9lqdgeBHDP6aPC8CYJM6cvRLtJnlEpqTotZaNZ7eeY71r%2F0gPzkMMLQLK%2B7mkwSdnBOnjnn2VFMJnxQIojawR3UHXushLl9U%2BjDTY6tIR8VtdhwBH0DGzBE%2FDjhBrBObYcccfr5jfjLNbf4LhjZ6Vd4mvqic0Mw2xHLS5UTnCaZdLdORJUmJ7LUM%2Bte9cnaGfoxrk1laP25tEQiQhIlZpQavSmJyVn4gbKvIA%2FulgDaf9gYTeFtJeiaUt8APIIveEyqFaVSkWSZZPUPjbgQ5YO6Tz74yfKzV%2Bit6qfj8MwEv6Xl6l2lY2hWQga%2FPPWzxYtZNoE1UrZCJmsFc%2F97cM6%2Fx9Q2SKyHXbkbUWGBI4Zp6EgO7ABr9I7gVPr8%2BOUO%2BOAjiGNnBFrtOJ1hAWrEA34KPhQiHd1HjToa%2B5nZAMuWLYGio9SuYIldMMrg5MgGOqUBV%2BXTma01eVl27RNuaaiz32Ds4S%2F1EyykardOmh9qsQYflE4EHqaDOZmrINcg9%2BSKdaeXvf6DwID6bNsC%2FqOp1otXJZ%2FyU%2BOHdKaGerxeE0Bgl3Tu%2FX0hh9%2FXXF6Ew52dIAzV4C9r39g2I62tTfiGWIUD6kd0dIo25nTUBOZ%2Fzvyf9NrNqOdWxidDc%2FkrNZVPae8nEDt9qk2LNi4yheDUqMG9k65j&X-Amz-Signature=da1725296d92cf0f88bbc2540936c88bb36eef088255f9a72c2ea22aeec9631e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5Y5TWCJ%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T062147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCW3ilGxNT8AvVccwgW4JcN7hhgXmyJbzYsHFZOY0NtQgIgErLCUc2NNs0GoOoMqrFB00Pj%2F6IJqjVxfi7qsH5ldhcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLU%2FgHmNYAZkf7Ko%2BircA7VhHqb8q8h9tiYPlffbBOsHVQtHGhTbIFf03F%2FcB2RFM%2F5jOsCr1uqQXI0sD5m%2FeixaescsDLg4mINzm8xKGoKwTcJMIXRIqEo12aTys6klv5RE5ywAbk8TpZv72dME78y6KnOil8KSYPXfGmoATWg1xYW6je36ZOaoRcgtwPhFTSpvJS%2FiU32FeR5LOZnmz2n%2Fx9lqdgeBHDP6aPC8CYJM6cvRLtJnlEpqTotZaNZ7eeY71r%2F0gPzkMMLQLK%2B7mkwSdnBOnjnn2VFMJnxQIojawR3UHXushLl9U%2BjDTY6tIR8VtdhwBH0DGzBE%2FDjhBrBObYcccfr5jfjLNbf4LhjZ6Vd4mvqic0Mw2xHLS5UTnCaZdLdORJUmJ7LUM%2Bte9cnaGfoxrk1laP25tEQiQhIlZpQavSmJyVn4gbKvIA%2FulgDaf9gYTeFtJeiaUt8APIIveEyqFaVSkWSZZPUPjbgQ5YO6Tz74yfKzV%2Bit6qfj8MwEv6Xl6l2lY2hWQga%2FPPWzxYtZNoE1UrZCJmsFc%2F97cM6%2Fx9Q2SKyHXbkbUWGBI4Zp6EgO7ABr9I7gVPr8%2BOUO%2BOAjiGNnBFrtOJ1hAWrEA34KPhQiHd1HjToa%2B5nZAMuWLYGio9SuYIldMMrg5MgGOqUBV%2BXTma01eVl27RNuaaiz32Ds4S%2F1EyykardOmh9qsQYflE4EHqaDOZmrINcg9%2BSKdaeXvf6DwID6bNsC%2FqOp1otXJZ%2FyU%2BOHdKaGerxeE0Bgl3Tu%2FX0hh9%2FXXF6Ew52dIAzV4C9r39g2I62tTfiGWIUD6kd0dIo25nTUBOZ%2Fzvyf9NrNqOdWxidDc%2FkrNZVPae8nEDt9qk2LNi4yheDUqMG9k65j&X-Amz-Signature=288f02b04aaee969c72a1643ff0d838343382105a345b1925fed2629ca3e8216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







