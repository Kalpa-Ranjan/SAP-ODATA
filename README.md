



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLR3WLLM%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T121153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD1BW4M5mBs3T%2FQ3j3MNu4cWDevsECR6yuUAmYfYdqj3QIhAP%2BzRlrCRhBG97Gzy2%2FB%2BkIIqCE8yjN7k7hiWn56OCn8KogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4pQpdDEGo9a4eGrcq3AMunxdmQakhvNtEohUX%2BQxVePpJvYFIrpjpU3GBLf%2B5yW2xBbOHPgsk7urEiK%2FbVRRk1xC3bcvaZFeZXKDW34qt8j4EiGPF5e8Qpr8RdfNGx8U4W%2FeKmP1mBu5G0W%2BL3g7qO3Uv8q7eelUoHTlbhA6gbZBBnXBtoQ3213%2FcjDdAU%2FStISoC0NO9cJCuuErfKmhA3hkTKzPgHuB7RGMpOAfD76zzc%2FkLN0moiyG84xPXj%2FN7YI%2FNFwmxNCiaBqfVU5uZi9lFKgjQZmlps941eBz1yoVtt9BZEoUwxCP0AB8YmK2i6gZ4HC6w7dsgTKEL5AwFIquIvSbN%2B89zlPDWQfyEYbMh972MV1TEX%2BjhhbplGgZ%2BL83%2BR%2B1dN6Tc%2FvVH%2BlqyaikssicBxO7P86jEBO%2B47lx7vfyFhZlVVIAe9%2BkcCW1nSzK4uP%2B2qZvkL0PFLV8GU1KUpc6H6BvK7ttn%2FXIS7Ocb7Q0EcEWIk55tj76ohE41%2B0aASmVz%2B%2BUJ%2Bg74RpTjKVWJGCgOG7cQmyw1hH4GvIVcaHssRW%2FoeRuORr2o5wGfO9xu9GuMUmiuaEyd1G24vZPMcdvTp6BvU2Li7X0huiJMBJboyw1W3XUciDKPELGOKnVIi98aNtGO1TDCmJPWBjqkAULeOZ4LClk3hGI1%2BznL%2FMeV9LehCYZ2QtSH3pkIxsdTkmEyHIoiAO1vyEGeMKsWBIh0CV%2Bh%2FFBJdU9ZYNEPv0qtNOonDN5yGfJvKCUxExsAcX3n9WgFwiljyv4sxXH%2BWZi%2F0iBjAzPsDFUcXPOwDaNT9elvLTg%2Ba6qZiLHlSc%2FZ7kpJsAlLS25KddHIQirFoIpqxU9tVziYzLU7BRdvclX1eIxa&X-Amz-Signature=bb90ede65252219b076b03e99dd28a4263f09d33307c844e535e1a8061fca5f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLR3WLLM%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T121153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD1BW4M5mBs3T%2FQ3j3MNu4cWDevsECR6yuUAmYfYdqj3QIhAP%2BzRlrCRhBG97Gzy2%2FB%2BkIIqCE8yjN7k7hiWn56OCn8KogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4pQpdDEGo9a4eGrcq3AMunxdmQakhvNtEohUX%2BQxVePpJvYFIrpjpU3GBLf%2B5yW2xBbOHPgsk7urEiK%2FbVRRk1xC3bcvaZFeZXKDW34qt8j4EiGPF5e8Qpr8RdfNGx8U4W%2FeKmP1mBu5G0W%2BL3g7qO3Uv8q7eelUoHTlbhA6gbZBBnXBtoQ3213%2FcjDdAU%2FStISoC0NO9cJCuuErfKmhA3hkTKzPgHuB7RGMpOAfD76zzc%2FkLN0moiyG84xPXj%2FN7YI%2FNFwmxNCiaBqfVU5uZi9lFKgjQZmlps941eBz1yoVtt9BZEoUwxCP0AB8YmK2i6gZ4HC6w7dsgTKEL5AwFIquIvSbN%2B89zlPDWQfyEYbMh972MV1TEX%2BjhhbplGgZ%2BL83%2BR%2B1dN6Tc%2FvVH%2BlqyaikssicBxO7P86jEBO%2B47lx7vfyFhZlVVIAe9%2BkcCW1nSzK4uP%2B2qZvkL0PFLV8GU1KUpc6H6BvK7ttn%2FXIS7Ocb7Q0EcEWIk55tj76ohE41%2B0aASmVz%2B%2BUJ%2Bg74RpTjKVWJGCgOG7cQmyw1hH4GvIVcaHssRW%2FoeRuORr2o5wGfO9xu9GuMUmiuaEyd1G24vZPMcdvTp6BvU2Li7X0huiJMBJboyw1W3XUciDKPELGOKnVIi98aNtGO1TDCmJPWBjqkAULeOZ4LClk3hGI1%2BznL%2FMeV9LehCYZ2QtSH3pkIxsdTkmEyHIoiAO1vyEGeMKsWBIh0CV%2Bh%2FFBJdU9ZYNEPv0qtNOonDN5yGfJvKCUxExsAcX3n9WgFwiljyv4sxXH%2BWZi%2F0iBjAzPsDFUcXPOwDaNT9elvLTg%2Ba6qZiLHlSc%2FZ7kpJsAlLS25KddHIQirFoIpqxU9tVziYzLU7BRdvclX1eIxa&X-Amz-Signature=cb6e21d67a41d6d49bb01908d62530889c9c38d0416008200be1439ec3de8cf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







