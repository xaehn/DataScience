import time
import random

# 설정
TOTAL_EPOCHS = 500  # 총 에폭 수
EPOCH_DURATION = 90 
SIMULATED_DURATION = 4 * 3600

# 학습 로그 출력 함수
def print_training_log(epoch, step, total_steps, accuracy, loss):
    print(f"Epoch {epoch}: Processing step {step}/{total_steps} | Current Accuracy: {accuracy:.4f} | Loss: {loss:.4f}")

#  학습 결과 생성 함수
def generate_results():
    accuracy = round(random.uniform(0.8, 0.999), 4)  # 임의의 정확도
    loss = round(random.uniform(0.001, 0.3), 4)  # 임의의 손실값
    return accuracy, loss

# 학습 프로세스 시뮬레이션
def simulate_training():
    start_time = time.time()
    epoch = 1

    print("AI model simulation is started")

    while True:
        # 에폭 진행
        print(f"===== [Epoch {epoch}/{TOTAL_EPOCHS}] =====")
        total_steps = random.randint(50, 100)  # 임의의 스텝 개수 설정
        for step in range(1, total_steps + 1):
            # 각 스텝별 학습 로그 출력
            accuracy, loss = generate_results()
            print_training_log(epoch, step, total_steps, accuracy, loss)
            time.sleep(EPOCH_DURATION / total_steps)  # 스텝별 시간 분배

        # 에폭 종료 메시지
        final_accuracy, final_loss = generate_results()
        print(f"\n[Epoch {epoch} is completed] Final Accuracy={final_accuracy:.4f}, Final Loss={final_loss:.4f}")
        print("-" * 60)

        # 다음 에폭으로 진행
        epoch += 1
        if epoch > TOTAL_EPOCHS:
            print("All epoch are completed")
            break

# 실행
simulate_training()