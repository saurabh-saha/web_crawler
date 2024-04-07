# Part 2: 

## Q: Provide design documentation to operationalize the collection of billions of URLs using the code developed.

###### Assumptions:
1 billion requests / day

###### Model Schema:
URL: 250 characters
Title: 100 characters
Description: 500 characters
Body: 5000 characters


## Calculation:

### Database:
1. Size of One Row = 250 bytes + 100 bytes + 500 bytes + 5000 bytes = 5.85 kb
2. DB Size Required for One Day = 5850 bytes/row * 1,000,000,000 rows ~= 5.85 TB
3. Data Stored in One Month: 5.85 TB/day * 30 days ≈ 175.5 TB
4. Total data for 1 month: Redundancy ~2 = 3 replicas ~= ≈ 526.5 TB

### Server:
1. throughput: 1 billion requests / day ≈ 11.5k requests per second

## Architecture Design:
### Server:
1. ECS : AWS container to handle incoming requests with Auto Scaling
2. NodeJS : async handling of requests to avoid website downtime, checks cache data
3. Flask : Flask worker node listen to SQS and process them, stores in mongo & cache

### Load Balancer:
AWS LB redirects traffic to ECS

### Queue:
SQS: NodeJS adds urls on SQS, read by flask worker nodes

### Cache:
Redis: for read through
Data Stored = 5.85 TB * 2 (1 replica) ~= 11TB
TTL : 1 day

## Q: Propose the next steps, how to further optimize for cost, reliability, performance, and scale.


### Reliability:
1. replication in redis, mongo. ECS for auto deployments
2. Health Checks and Monitoring of node & flask ECS nodes
3. Backup of all services

### Performance:
1. Caching in redis
2. mongo - Indexing Optimization

### Scale:
Horizontal Scaling - ECS more nodes
Distributed Processing: SQS
Global Load Balancing

### Configurability, Politeness, and Respect for Robots.txt:
1. Configuration in .env files of crawl frequency
2. Rate Limiting: based on IP address, URL path in LB

## Monitoring Metrics and Tools
### System Metrics:
1. Monitor ECS, redis, mongo usage - CPU utilization, memory usage, and network traffic 
2. Crawl Metrics: Monitor crawl throughput, latency, and error rates

# Part 3: 

### Q: proceed with engineering to Proof of Concept

1. Gather Non-functional Requirement for PoC use case. Find only the imp params.
   1. max requests per second with a response time of under x ms. 
   2. support x billion URLs 
   3. uptime of 99.9% 
   4. HTTPS encryption and access controls 
   5. modular code architecture
2. Gather functional reqs for the PoC.
   1. crawl HTML content from provided URLs. 
   2. Extract title, description, and body content from crawled URLs. 
   3. Classify URLs into topics or categories based on metadata. 
   4. Implement rate limiting 
3. Finalise Architecture
   1. Tech Stack: Python Flask for backend, MongoDB for metadata storage, Redis for caching
   2. AWS services (ECS, SQS, ALB) for infrastructure. 
   3. Database : Deploy MongoDB for metadata storage
5. Finalise Testing required : 
   1. Unit Tests: Test individual components such as URL crawler, metadata extractor, and classifier. 
   2. End-to-End Tests: Validate end-to-end functionality 
   3. Load Testing: Test system performance under high loads to ensure scalability and reliability.
6. Define Deployment strategy for PoC. 
   1. Deploy the PoC 
   2. Use Terraform for infrastructure as code to automate deployment.
7. Documentation these in a TRD
   1. Project Plan: Detailed breakdown of tasks, milestones, and timelines.
   2. Testing Plan: Outline of testing strategies, methodologies, and success criteria.
   3. Roles and Responsibilities Matrix: Matrix mapping team members to specific roles and responsibilities.
   4. Release Schedule: Timeline for planned releases, including feature rollout and updates.
   5. Resource Allocation: Breakdown of resource requirements and estimated costs.
   6. Limitations

### Limitations
1. Robots.txt Restrictions have to be adhered meaning some pages may not be crawled. should we just list these pages as not accessable ?
2. Rate Limiting and IP Blocking have to identified or solutions of work around will be needed. Needs RnD
3. Dynamic Content and JavaScript Rendered websites have to identified and marked appropriately.
4. CAPTCHAs and Human Verification based websites also need to be identified and marked not-accessible.
5. Session-based Authentication need to identified and if possible session based solution to be developed.
6. Legal and Ethical Considerations: Crawling websites without permission - discuss with PM 
7. Technical Challenges: error handling and retry mechanisms.