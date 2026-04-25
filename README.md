



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTKZK6M3%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T070720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdmyWntncuj2g1jBsLStFMo%2FzUc6QlpMl8pt5jQVsshAiASVFhHq4QjAI0g7qiDrrioxPhw6yjJj9UjB6g4zrijWCqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxTXbytm%2Fkzw1ldjiKtwD0FhMizgzIalc0%2BZ%2F9s%2BFTgI%2BK7XeaZeDB2ZZSN%2B6vMpNtHzN8clo2C5wCHYcH2N9IlBgHPPxbs22mQMV6L9ISKFrfUBQPvS9j5XVgwNw5JG9wGQBjsEtZ6WxBu2m2KuPdGz3NE3s0TgptuKHf0eScmAdNEcrVzsUg1sxe0B2hiebPY8n8uBKaPxhD9Eul7c9%2FnmQI%2BGba6fr0jVmN38MjUtOiJxeWC4ZHL9T7G%2Fui9eDUbU9woRbggTl79IwozQWLVHNP06TvT70vwrJO9R%2F9wmAEZL8KwKiOquIoNteOb36ueX3%2BqqyDYTd18L5cUQvAxZuoZSkqkRx1Y3tikWHbwEe71wq%2Fm5p6UK3jTQG8wdDDxBx8AqKmC0RdVFNzuWybI0EbGCIC5AvkkKYMvzrQZBestvr1Z9EqKZhuA3y3FN4xzhhfr0jE3w7bQYjZ2WOBrShvI0SWS8UGM%2FM8J0G4%2BupIEn21kQh8%2F4pQB6%2BRJQAZ9xSm%2BVkGNvly%2BWWW1SZoLTitk%2FvxbBTc0AOgpIOS9eYJuA%2BU0EO7zAD60GdBEts8jAYa4KtyDsqkaLHd4ixs0RDzVume2oUafBW8sJquNQv6kgeRhDfeMQivHzobwq9fZlxRPS9mH6xIK0wja%2BxzwY6pgFaymFtHa9rkCfK4e5h7rlloY9eKFa2iUQohGUenGQK%2FRb5WtMU1OiHkT667h8fdzHUMlAftFkcSUU%2B0Q1S30gopz2Cmn6c2i9knvhv3a4OOpqerP2F9xBO%2FeeUiCMwrhq0U5M4LMw9m%2FWRuL4ewgK6rMXx6jldf%2BVuAtu028eNWd4su5enIYzhLrokJTBlEzm3jDqAC04ojvfiangnsRkOJXCJosdf&X-Amz-Signature=8f10eae059bc3232f7d73e85f8d999f750536b72ebf1520b20afe509dae2560a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTKZK6M3%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T070721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdmyWntncuj2g1jBsLStFMo%2FzUc6QlpMl8pt5jQVsshAiASVFhHq4QjAI0g7qiDrrioxPhw6yjJj9UjB6g4zrijWCqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxTXbytm%2Fkzw1ldjiKtwD0FhMizgzIalc0%2BZ%2F9s%2BFTgI%2BK7XeaZeDB2ZZSN%2B6vMpNtHzN8clo2C5wCHYcH2N9IlBgHPPxbs22mQMV6L9ISKFrfUBQPvS9j5XVgwNw5JG9wGQBjsEtZ6WxBu2m2KuPdGz3NE3s0TgptuKHf0eScmAdNEcrVzsUg1sxe0B2hiebPY8n8uBKaPxhD9Eul7c9%2FnmQI%2BGba6fr0jVmN38MjUtOiJxeWC4ZHL9T7G%2Fui9eDUbU9woRbggTl79IwozQWLVHNP06TvT70vwrJO9R%2F9wmAEZL8KwKiOquIoNteOb36ueX3%2BqqyDYTd18L5cUQvAxZuoZSkqkRx1Y3tikWHbwEe71wq%2Fm5p6UK3jTQG8wdDDxBx8AqKmC0RdVFNzuWybI0EbGCIC5AvkkKYMvzrQZBestvr1Z9EqKZhuA3y3FN4xzhhfr0jE3w7bQYjZ2WOBrShvI0SWS8UGM%2FM8J0G4%2BupIEn21kQh8%2F4pQB6%2BRJQAZ9xSm%2BVkGNvly%2BWWW1SZoLTitk%2FvxbBTc0AOgpIOS9eYJuA%2BU0EO7zAD60GdBEts8jAYa4KtyDsqkaLHd4ixs0RDzVume2oUafBW8sJquNQv6kgeRhDfeMQivHzobwq9fZlxRPS9mH6xIK0wja%2BxzwY6pgFaymFtHa9rkCfK4e5h7rlloY9eKFa2iUQohGUenGQK%2FRb5WtMU1OiHkT667h8fdzHUMlAftFkcSUU%2B0Q1S30gopz2Cmn6c2i9knvhv3a4OOpqerP2F9xBO%2FeeUiCMwrhq0U5M4LMw9m%2FWRuL4ewgK6rMXx6jldf%2BVuAtu028eNWd4su5enIYzhLrokJTBlEzm3jDqAC04ojvfiangnsRkOJXCJosdf&X-Amz-Signature=9e65beab791fce7dcbfce65d229205b2d1bc65bf65f08f0d76b4bef70649dbb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







