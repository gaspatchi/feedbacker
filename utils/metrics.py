from prometheus_client import CollectorRegistry, Counter, generate_latest
import prometheus_client

registry = CollectorRegistry()

created_feedbacks = Counter("feedbacker_created_feedbacks", "Количество созданых обращений", ["type"], registry=registry)
count_feedbacks = Counter("feedbacker_selects_count_feedbacks", "Количество получений обращений", registry=registry)