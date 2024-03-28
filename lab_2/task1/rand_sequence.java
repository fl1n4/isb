import java.util.Random;

public class RandomSequenceGenerator {
    public static String generateRandomSequence() {
        StringBuilder sequence = new StringBuilder();
        Random random = new Random();

        for (int i = 0; i < 128; ++i) {
            sequence.append(random.nextInt(2));
        }

        return sequence.toString();
    }

    public static void main(String[] args) {
        String randomSequence = generateRandomSequence();
        System.out.println("Generated Sequence: " + randomSequence);
    }
}