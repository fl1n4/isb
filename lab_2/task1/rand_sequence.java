import java.util.Random;

/**
 * Utility class for generating random binary sequences.
 */ 
public class RandomSequenceGenerator {
    /**
     * Generates a random binary sequence of length 128.
     *
     * @return A string containing a random binary sequence.
     */
    public static String generateRandomSequence() {
        StringBuilder sequence = new StringBuilder();
        Random random = new Random();

        for (int i = 0; i < 128; ++i) {
            sequence.append(random.nextInt(2));
        }

        return sequence.toString();
    }
    
    /**
     * Main method to demonstrate the usage of the generateRandomSequence method.
     *
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        String randomSequence = generateRandomSequence();
        System.out.println("Generated Sequence: " + randomSequence);
    }
}