



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663S6HLLSZ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T014118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUI2lbQdKPBtcEaYteJnXqE50A1ego%2F9EdpxaSg2D0wAIgHOt9haHaiL7t%2BJqBDfO5c5%2Bvh5UWWhCuGIV4v2FYTm4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKf6WTkUsCLASk990SrcA6H50jPmNUxRdtjqsOT%2Fe5mPoNjZbE%2F4yBT6T0XWtPejpnvKZgv6wzbTV8kQG3bya25gLZi6GhhvSJ6Y7ahRiWjIy7aMmVwh5n4rD1xblhMWSDwrCIP7nL%2BKupsPdOa8SBhiCGKXOhmhUQK9k273T1WszaikZKD67i%2B8dmKxXm7pF6ktyyAGx0mRdKc3Q%2FjxMB8NOizWLjzjlmgfaraDNbmcs1ibEjvtuKmZKyVzjMzYdCUe9zZ%2FA1qb8q55Myppa3smzs8LUZ1oqyw7M0cflu5GLIX5LOVD9atkOh4MBlK4lqpkD2kyJwf%2FBWXm9rFMddYo1kLUl63drKx03D9gJD4UKymQ2w0yL1kRfStTydtqSsuto8h1P211RNLybntNG9f7GaODiuMB%2F%2B19ke5eIVMki8Ig4EKsuMnkqAId719RSrWaA9Oq2TGw25Vv5nXqsH6X9EGOttOEQKnbCycxZSrB9H7ot3ygxietPR%2FHC%2FWbof%2F%2FJDY1grOCkm%2FQ8FIOU8zpVEufY7A3beJsWo0lFrJlFtixgWnLVmtle7hFA7SKN0ccV7kfiDa43hcIDH48URq5AVVr5%2F9CjWHbZN1RfU%2BneZ4m3v19AowsIT%2BlALrE14aabInmfJEdSMmxMKXd6ssGOqUBQNf2osnJ1Pz8bflTHgs%2ByBB72kSdEgM0fZlbZR5SzyHee80yhDs171FNQC9SxJZYCsRl4oI1H4Wc1Nu9to87RtulbpOnlUfRyg9kEc67HgkQBLwi9%2FnfY6gHsOvJFx7toeQu6mwnhyuazZPrqmdHROr29DxxkaDO2R4zlReQnlKPbLmi%2BTwn%2BcpibZlWYXMjnfGo7bmJdSjS1%2BFO42NlqtR339FB&X-Amz-Signature=1d4e892c964de686b3060017f65bdf660aa1f0f25626332454c57cc79d955570&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663S6HLLSZ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T014119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUI2lbQdKPBtcEaYteJnXqE50A1ego%2F9EdpxaSg2D0wAIgHOt9haHaiL7t%2BJqBDfO5c5%2Bvh5UWWhCuGIV4v2FYTm4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKf6WTkUsCLASk990SrcA6H50jPmNUxRdtjqsOT%2Fe5mPoNjZbE%2F4yBT6T0XWtPejpnvKZgv6wzbTV8kQG3bya25gLZi6GhhvSJ6Y7ahRiWjIy7aMmVwh5n4rD1xblhMWSDwrCIP7nL%2BKupsPdOa8SBhiCGKXOhmhUQK9k273T1WszaikZKD67i%2B8dmKxXm7pF6ktyyAGx0mRdKc3Q%2FjxMB8NOizWLjzjlmgfaraDNbmcs1ibEjvtuKmZKyVzjMzYdCUe9zZ%2FA1qb8q55Myppa3smzs8LUZ1oqyw7M0cflu5GLIX5LOVD9atkOh4MBlK4lqpkD2kyJwf%2FBWXm9rFMddYo1kLUl63drKx03D9gJD4UKymQ2w0yL1kRfStTydtqSsuto8h1P211RNLybntNG9f7GaODiuMB%2F%2B19ke5eIVMki8Ig4EKsuMnkqAId719RSrWaA9Oq2TGw25Vv5nXqsH6X9EGOttOEQKnbCycxZSrB9H7ot3ygxietPR%2FHC%2FWbof%2F%2FJDY1grOCkm%2FQ8FIOU8zpVEufY7A3beJsWo0lFrJlFtixgWnLVmtle7hFA7SKN0ccV7kfiDa43hcIDH48URq5AVVr5%2F9CjWHbZN1RfU%2BneZ4m3v19AowsIT%2BlALrE14aabInmfJEdSMmxMKXd6ssGOqUBQNf2osnJ1Pz8bflTHgs%2ByBB72kSdEgM0fZlbZR5SzyHee80yhDs171FNQC9SxJZYCsRl4oI1H4Wc1Nu9to87RtulbpOnlUfRyg9kEc67HgkQBLwi9%2FnfY6gHsOvJFx7toeQu6mwnhyuazZPrqmdHROr29DxxkaDO2R4zlReQnlKPbLmi%2BTwn%2BcpibZlWYXMjnfGo7bmJdSjS1%2BFO42NlqtR339FB&X-Amz-Signature=6f4c7e5accdfc18b5bc7a580cf569f70393c0af316a21d882c07b0e19f88770f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







