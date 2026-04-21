



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NX76E6N%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T190459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCYJRXqYKidU0zXSwStSo%2BO2L%2FHpI2t6Fwp65ARLvY6rQIhAJtVuW6FdtxahSzJEd5%2F9HfoeRnY5rq0n7Ujw0NhC51RKv8DCDsQABoMNjM3NDIzMTgzODA1IgzsDGRaeJ01e6Vjk3Iq3AMLtbsPGRhQAWYUFeSzPlgE0mR8d%2FW2rgl7d66hv2j3ZEtvZEe0AstWgAo6HHMuqrYuqKCeexrAuD1xEKWf4Vskulfo0LgTChNo6bu1XgvevUmcyd79pqRSPqmLJh9a%2FT7a76Rr%2FID3BjGZ5o0qHCeurruGYjNp7FEH%2Byn355uJg8TtPuktgtBhRAx4mKUU9IDq%2Fn%2BWVg6JuZrYt7dN%2Bxg4g%2FIx05JbbccZZiqnW4%2BjkUKv0wiYkxEoJTkwruCjO1pfn0tnnEyf2Rv2tmECZDejaYPI7X7LAI5CnYug7EjqfJM9IvRBCzS7nkNXzUVMf08sH%2BqZC6BfDKq3OdjJB2V8Tft7wuZwQY3OXBau9M5hS9WvKN4QP76ZqX4CNXJNdy4Ux%2FzL7smphKivTBDAVXq6OBoEv85HCrtsKl3ZpdkqQ39wJ2%2FP%2BdECGsHvRa44rSZ5UMGVF%2FgWJjxRAicOl54hAyDUyxlgZR4QtaQ4%2FZkoKD7JfXqenHoHRfnkR6aFvWHtzzjuF0plopCKNUXulqdT1fZ3b%2BEtCGG7Dho%2BMVOOJ3LbdIKkym3a69mMOG%2BDc5WJTS5W4V3XhApvv5tnuK%2BbRpGCziPGqmf1DUQdDMWOnoLDsBSyO3G%2B06jFaDDQ%2BZ7PBjqkAdRApHc7oiwN87oevwPecYcmhpDNvFxf3CfDgeLc4CUZqbNH%2Fn6APoTSNorXA9%2Broi44DTgD40yK6WMAmzRD%2FbAdWL6lYeIOMg68ECSuNiOEcpPfJjpXWyF4ftap4Ya6DygeDZGZ1Nr%2B3FWPMVikmxq45ri6cKJMM1mTieecSUZaORnubxZJtBdPzFukUIu99rM5m4z6R22SpdIU3wmeBokO9D0f&X-Amz-Signature=09ceccba434db4d0d3922fe5e6a3e258d2072d146d25daa3f24c4718a393094f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NX76E6N%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T190459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCYJRXqYKidU0zXSwStSo%2BO2L%2FHpI2t6Fwp65ARLvY6rQIhAJtVuW6FdtxahSzJEd5%2F9HfoeRnY5rq0n7Ujw0NhC51RKv8DCDsQABoMNjM3NDIzMTgzODA1IgzsDGRaeJ01e6Vjk3Iq3AMLtbsPGRhQAWYUFeSzPlgE0mR8d%2FW2rgl7d66hv2j3ZEtvZEe0AstWgAo6HHMuqrYuqKCeexrAuD1xEKWf4Vskulfo0LgTChNo6bu1XgvevUmcyd79pqRSPqmLJh9a%2FT7a76Rr%2FID3BjGZ5o0qHCeurruGYjNp7FEH%2Byn355uJg8TtPuktgtBhRAx4mKUU9IDq%2Fn%2BWVg6JuZrYt7dN%2Bxg4g%2FIx05JbbccZZiqnW4%2BjkUKv0wiYkxEoJTkwruCjO1pfn0tnnEyf2Rv2tmECZDejaYPI7X7LAI5CnYug7EjqfJM9IvRBCzS7nkNXzUVMf08sH%2BqZC6BfDKq3OdjJB2V8Tft7wuZwQY3OXBau9M5hS9WvKN4QP76ZqX4CNXJNdy4Ux%2FzL7smphKivTBDAVXq6OBoEv85HCrtsKl3ZpdkqQ39wJ2%2FP%2BdECGsHvRa44rSZ5UMGVF%2FgWJjxRAicOl54hAyDUyxlgZR4QtaQ4%2FZkoKD7JfXqenHoHRfnkR6aFvWHtzzjuF0plopCKNUXulqdT1fZ3b%2BEtCGG7Dho%2BMVOOJ3LbdIKkym3a69mMOG%2BDc5WJTS5W4V3XhApvv5tnuK%2BbRpGCziPGqmf1DUQdDMWOnoLDsBSyO3G%2B06jFaDDQ%2BZ7PBjqkAdRApHc7oiwN87oevwPecYcmhpDNvFxf3CfDgeLc4CUZqbNH%2Fn6APoTSNorXA9%2Broi44DTgD40yK6WMAmzRD%2FbAdWL6lYeIOMg68ECSuNiOEcpPfJjpXWyF4ftap4Ya6DygeDZGZ1Nr%2B3FWPMVikmxq45ri6cKJMM1mTieecSUZaORnubxZJtBdPzFukUIu99rM5m4z6R22SpdIU3wmeBokO9D0f&X-Amz-Signature=263d33e6536a09c8ccf700e9a2b8fe628401aa3a17784752f070d5d3bab75034&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







