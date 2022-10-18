package org.mds.experimental;


import io.netty.handler.codec.string.LineSeparator;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

@Slf4j
public class DataSource {
    public final static String DATA_URL = "https://gist.githubusercontent.com/pxsdirac/940436aa85580ac3d72a8cce8cbcc022/raw/aeb7da0710bb87b5106b7b564f40ac4c538fc9a5/movie.csv";
    private WebClient webClient;

    public DataSource() {

        this.webClient = WebClient.create(DATA_URL);
    }

    public Mono<List<Data>> data(int count) {
        return this.webClient.get().retrieve()
                .toEntity(String.class)
                .flatMapMany(stringResponseEntity ->
                        Flux.fromIterable(this.readLineData(Objects.requireNonNull(stringResponseEntity.getBody()))))
                .sort((o1, o2) -> Float.compare(o1.getRating(), o2.getRating()))
                .take(count).collectList();
    }

    private List<Data> readLineData(String s) {
        List<Data> ret = new ArrayList<>();
        String[] lines = s.split(LineSeparator.UNIX.value());
        for (int i = 1; i < lines.length; i++) {
            Data data = new Data();
            List<String> fields=new ArrayList<>();
            if (lines[i].startsWith("\"")) {
                int splitIndex = lines[1].indexOf("\"", 1);
                fields.add(lines[i].substring(1, splitIndex));
                String[] otherFields = lines[i].substring(splitIndex + 2).split(",", 3);
                fields.addAll(Arrays.asList(otherFields));
            } else {
                fields.addAll(Arrays.asList(lines[i].split(",", 4)));
            }
            data = this.setDataFields(data, fields);
            if (data != null) ret.add(data);         
        }

        return ret;
    }

    private Data setDataFields(Data data, List<String> fields) {
        try {
            data.setName(fields.get(0))
                    .setRuningTime(Float.parseFloat(fields.get(1)))
                    .setRating(Float.parseFloat(fields.get(2)))
                    .setTitle(fields.get(3));
            return data;
        } catch (Exception ex) {
            log.warn("invalid data: ");
        }
        return null;
    }
}
