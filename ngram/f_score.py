def f_score(input_file, output_number):

    with open(input_file, 'r') as input:
        content = input.readlines()
        answer_num = len(content)

        predict_correct_num = 0
        predict_words = []

        for item in content:
            result = item.strip().split('\t')
            correct = result[0].split(' ')[2]

            for i in range(1, len(result)):
                try:
                    float(result[i])
                except:
                    predict = result[i].split(' ')[2]
                    predict_words.append(predict)
            print(correct)
            print(predict_words)
            if correct in predict_words:
                predict_correct_num += 1

            predict_words = []

    recall = predict_correct_num / output_number
    precision = predict_correct_num / answer_num
    f_score = 2/(1/precision + 1/recall)